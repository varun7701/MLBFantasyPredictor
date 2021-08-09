"""Setup at app startup"""
from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
from flask import render_template, request, jsonify, redirect, url_for, render_template

mysql = MySQL(app)

app.config['MYSQL_HOST'] = '34.68.2.154'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '7153'
app.config['MYSQL_DB'] = 'player'
 


# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position

@app.route("/", methods = ['GET'])
def homepage():
    """ returns rendered homepage """

    cur = mysql.connection.cursor()
    cur.execute("SELECT * From Players")
    rows = cur.fetchall()
    todo_list = []
    for result in rows:
        item = {
            "PlayerName": result[0],
            "TeamName": result[1]
        }
        todo_list.append(item)
    mysql.connection.commit()
    cur.close()
    
    return render_template("index.html", Players=todo_list)

@app.route("/searchPlayer", methods = ['GET', 'POST'])
def search():

    PlayerName = request.form['PlayerName']
    PlayerName = str(PlayerName)
    cur = mysql.connection.cursor()
    query = "SELECT * FROM Players WHERE PlayerName LIKE '%{}%';".format(PlayerName)
    cur.execute(query)
    rows = cur.fetchall()
    todo_list = []
    for result in rows:
        item = {
            "PlayerName": result[0],
            "TeamName": result[1]
        }
        todo_list.append(item)
    mysql.connection.commit()
    cur.close()
    return render_template("list.html", Players=todo_list)

@app.route('/edit/<string:PlayerName>', methods = ['POST', 'GET'])
def get_player(PlayerName):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Players WHERE PlayerName = "{}";'.format(PlayerName))
    data = cur.fetchall()
    cur.close()
    return render_template('edit.html', player = {"PlayerName" : PlayerName}) 


@app.route('/update/<string:PlayerName>', methods=['POST'])
def update(PlayerName):
    """ recieved post requests for entry updates """
    print(PlayerName)
    if request.method == 'POST':
        TeamName = request.form["TeamName"]
        cur = mysql.connection.cursor()
        query = 'UPDATE Players SET TeamName = "{}" WHERE PlayerName = "{}" ;'.format(TeamName, PlayerName)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('homepage'))



@app.route("/delete/<string:PlayerName>", methods=['POST'])
def delete(PlayerName):
    """ recieved post requests for entry delete """

    
    cur = mysql.connection.cursor()
    query = 'Delete FROM Players WHERE PlayerName = "{}";'.format(PlayerName)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
        
    return redirect(url_for('homepage'))



@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    #data = request.get_json()
    if request.method == 'POST':
        PlayerName = request.form["PlayerName"]
        TeamName = request.form["TeamName"]
        cur = mysql.connection.cursor()
        query = 'Insert Ignore Into Players (PlayerName, TeamName) VALUES ("{}", "{}");'.format(PlayerName, TeamName)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
  
    return redirect(url_for('homepage'))


@app.route("/query1", methods=['GET', 'POST'])
def query1():
    """ returns query 1 results """

    cur = mysql.connection.cursor()
    cur.execute("SELECT p.TeamName, AVG(b.G) as avg_games_for_team, AVG(b.OPS) AS avg_OPS FROM Players p JOIN Batter b ON p.PlayerName = b.playerName GROUP BY p.TeamName ORDER BY avg_games_for_team DESC, avg_OPS DESC;")
    rows = cur.fetchall()
    
    player = []
    for result in rows:
        item = {
            "TeamName": result[0],
            "G"       : result[1],
            "OPS"     : result[2]
        }
        player.append(item)
    
    mysql.connection.commit()
    cur.close()

    return render_template("query1.html", Players=player)

@app.route("/query2", methods=['GET', 'POST'])
def query2():
    """ returns query 2 results """

    cur = mysql.connection.cursor()
    cur.execute("(SELECT p.PlayerName, p.TeamName, 'Batter' as Role FROM Players p JOIN Batter b ON p.PlayerName = b.PlayerName WHERE b.HR >= 10 AND p.TeamName = 'CHC' ORDER BY b.HR DESC LIMIT 13) UNION (SELECT p.PlayerName, p.TeamName, 'Pitcher' as Role  FROM Players p JOIN Pitcher pi ON  p.PlayerName = pi.PlayerName WHERE pi.W >= 7 AND p.TeamName = 'CHC' ORDER BY pi.W DESC LIMIT 12);") 
    rows = cur.fetchall()
    players = []
    for result in rows:

        item = {
            "PlayerName": result[0],
            "TeamName": result[1],
            "Role": result[2]
        }
        players.append(item)
    mysql.connection.commit()
    cur.close()

    return render_template("query2.html", Players=players)


@app.route("/recommendations", methods=['GET', 'POST']) 
def storedProcedure(): 
    
    cur = mysql.connection.cursor() 

    cur.callproc('Recommendations',())

    fantasy = [] 
    stats = [] 
    teams = []

    rows = cur.fetchall()

    for result in rows:

        item = {
            "PlayerName": result[0],
            "TeamName": result[1],
            "Points": result[2], 
            "Role": result[3],
            "Grade": result[4]
        }
        fantasy.append(item)
    
    count = 1

    while(cur.nextset()):
       
        if count == 1: 

            rows = cur.fetchall()

            for result in rows:

                item = {
                    "PlayerName": result[0],
                    "TeamName": result[1],
                    "Stat": result[2], 
                    "Role": result[3],
                    "Grade": result[4]
                }
                stats.append(item)
        
        if count == 2: 
           
            rows = cur.fetchall()

            for result in rows:

                item = {
                    "TeamName": result[0],
                    "Avg_Points": result[1],
                    "League": result[2], 
                    "Division": result[3],
                    "Grade": result[4]
                }
                teams.append(item)
        
        count += 1

    return render_template("recommendations.html", Fantasy = fantasy, Stats = stats, Teams = teams)

   
    

