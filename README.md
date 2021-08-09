# MLBFantasyPredictor
CS411, University of Illinois at Urbana-Champaign
Summer 2021
 
 
 
 
 
 
Final Project Report:
MLB Player Predictor
 
 
 
 
 
 
 
Nikhil Khandekar
Varun Vangala
Yashowardhan Maheshwari
Matthew Weiler
 
 
 
What Did Our Project Accomplish?
 
MLB Fantasy Predictor is an application for users to be able to interact with a database of players and their teams while also providing recommendations for players and teams to invest on. Specifically, a user will be able to insert a player and their team, be able to search for a player by their name, edit a player’s team, and also delete a player. A user will also be able to get recommendations for top performing players and teams based on their overall batting and pitching statistics or their fantasy points. 
 
 
Utility of our Project
 
	Finding the ideal players and teams to invest on can be very challenging for MLB fantasy players, and so we wanted to design an application to report to users the best players and teams over the years. While there are applications which can do predictions, the algorithms are often faulty in that they only look at batter and pitcher statistics as opposed to looking at fantasy statistics as well for a given player. Our project improves upon other existing recommendation sites by providing insights to users on top players based on fantasy points and statistics. In addition, we also give a grade between A, B, and C which is used as an overall rating to tell how valuable we think a player is, which should help indicate to a user that they should choose this player in their fantasy pick. Additionally, in allowing users to search, pick, add, and remove players, we are allowing them to have control of a database which will allow them to update the database in a way that they choose to keep track of players that they care about the most. This is different from other applications where individuals have no control over the database at all.
 
Our Data
 
           The data in our database were meant to describe and categorize the different players and teams in MLB. We had a database called Teams which provided information about the team name, their league, division, and the number of players in each team. The Players table was meant to store information about all players playing in the 2021 season. The table included information about player names and the teams that they play for. The Batters table stores information of all batters in the 2021 MLB season which includes the player name, the number of games, and their batting statistics which will be further specified in the UML diagram. Similarly, the Pitchers table stores information about players in the 2021 MLB season and includes information about their pitching statistics which will be further specified in the UML diagram. Lastly, we had a table called FantasyPoints which was meant to give the fantasy points of all players, both batters and pitchers. This table includes information about the player name and the number of fantasy points that they have. In all, these were used in helping make predictions on the best players and teams which is why we included them for our project. 
UML Diagram
 

 
 
 
 
 
 
 
 
 
 
 
DDL Commands
CREATE TABLE Players(PlayerName VARCHAR(50) NOT NULL, TeamName VARCHAR(3), PRIMARY KEY (PlayerName)); 
CREATE TABLE FantasyPoints(PlayerName VARCHAR(50) NOT NULL, POINTS INT, PRIMARY KEY(PlayerName), FOREIGN KEY (PlayerName) REFERENCES (PlayerName)); 
CREATE TABLE Pitcher(PlayerName VARCHAR(50) NOT NULL, G INT, GS INT, CG INT, SHO INT, IP REAL, H INT, ER INT, K INT, BB INT, HR INT, W INT, L INT, SV INT, BS INT, HLD INT, ERA REAL, WHIP REAL, PRIMARY KEY(PlayerName), FOREIGN KEY (PlayerName) REFERENCES Players(PlayerName)); 
CREATE TABLE Batter(PlayerName VARCHAR(50) NOT NULL, G INT, AB INT, R INT, H INT, twoB INT, threeB INT, HR INT, RBI INT, SB INT,CS INT, BB INT, SO INT, SH INT, SF INT, HBP INT, batting_avg REAL, OBP REAL, SLG REAL, OPS REAL, PRIMARY KEY (PlayerName), FOREIGN KEY (PlayerName) REFERENCES Players(PlayerName)) 
 
Indexing Design 
 
All of our indexing design images were all directly taken from part 3. 
 
First query: 

 
Initial indexing: 
 
Index just on Players: 
 
Results from EXPLAIN-ANALYZE command:  

 
 
Execution Time: 0.04s

 
 
Index using TeamName for query 1: 
 
 
 
 
Results from EXPLAIN ANALYZE command: 
 

 
Execution time: 0.03 s
 

 
 
Index using Game for query 1: 
 
All indices: 
 

 
Using the EXPLAIN-ANALYZE command: 
 

 
Execution time: 0.03 s
 
Execution diagram: 
 

 
 
 
Index using Game and OPS for query #1: 
 
Indices being used:  
 

 
Using the EXPLAIN-ANALYZE command:  
 
 
 
Execution time: 0.03 s
 
 
 
 
Execution Plan: 

 
 
 
 
 
Analysis and Justification: 
 
Without indexing the query cost was 529.35, and with any sort of indexing that we tried, the query cost was 514.95 and the overall time reduced from 0.04 seconds to 0.03 seconds. We are not sure why the query cost values are the same for the different indexing that we tried but we are not surprised that the query cost did not decrease by much because in all cases, we would still need to go through the whole table when wanting to compute the averages of of player's games and their OBS and so having the data arranged by any specific attribute will not improve the query performance by much. Hence, we will not be indexing on this table as there is a negligible difference in query cost and query speed difference. 
 
 
Query #2: 
 

 
 
 
Initial indexing: 
 

 
 
Results from EXPLAIN-ANALYZE command: 
 

 
Execution: 0.04 s
 
 
 
 
Execution Plan: 

 
 
 
Indexing using TeamName using Query 2: 
 

 
Results from EXPLAIN-ANALYZE command: 
 

Execution Time: 0.03 s
 
Execution Plan: 
 

Indexing on Homeruns: 
 
Indexes: 
 

 
EXPLAIN-ANALYZE command: 
 

 
Execution time: 0.03 s 
 
Execution Plan: 

 
 
 
Indexing on Home Runs and Wins: 
 
Indexes: 
 

 
 
Indexes: 
 

 
Results from the EXPLAIN-ANALYZE command: 
 

 
Execution time: 0.03 s
 
Execution Diagram: 

 
Analysis and Justification: 
Overall, we do not plan on indexing as the time decrease is only 0.01 seconds. While the query cost is smaller when indexing on a particular value, this is not appreciable as there are only a small number of rows. The decrease in query cost when indexing likely came because the indexes were sorted by those attributes, making it easier to identify specific values and query and return those records. 
 
Data Collection Sources and Process
 
We collected our data from various websites that organize CSV files of MLB players, teams, on-field statistics, and Fantasy Baseball data. Rotowire.com provided us with data for MLB players and their on-field pitching and batting statistics, such as batting averages and on-base percentages for batters and Earned Run Average (ERA) for pitchers. Furthermore, CBS Fantasy Baseball compiles Fantasy Baseball data from recent years in CSV files that we were able to use for that context of data. We simply created our database schema in MySQL Workspace using the above DDL commands, and imported our CSVs. 
 
Application Design, Features, and Functionality
 
The main functionality in our application design is the ability for a user to interact with a database of all MLB players and their teams, assisting them in constructing their Fantasy Baseball team with maximum point potential. Upon loading the webpage, the user is presented with a table of all MLB players and the team that each of them play for. There is also a notepad logo, which can be clicked to edit the player entry, and a trash can logo, which can be used to delete the player entry. Moreover, the homepage has an “Add Player” button. Upon clicking, the user is redirected to a form where they can enter a player and their team to be added to the database.  A user can also search for a player’s name, either in full or just a few letters, in the database using the Search Bar. Furthermore, an important feature of the application is the automated Recommendation System. Upon the click of a button, the user can view the top 15 players and teams in various categories: Total Fantasy Points, On-Field Statistics, Average Team Fantasy Points. Each of these players are also assigned grades, which give the user insight on which players might be best for them to pick up. If a player has a B grade, for example, their current statistics might not be amazing, but they show good potential to be successful on a fantasy team. 
 
 
 
 
 
 
 
 
 
 
 
 
Advanced Database Program: Player Recommendation System
 
 
The following code is used for our stored procedure: 
 






 

 



Code for connecting MySQL workbench to the main application: 
 
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
 
 
 
Code for triggers: 
 
AFTER INSERT: 
 

 
 
 
 
AFTER UPDATE:

 
AFTER DELETE: 
 

 
Our Player Recommendation System was implemented using a stored procedure. The recommendation returns three tables to the user: Top Players in terms of Fantasy Points and On-Field Stats, as well as one for Top Teams in terms of Average Fantasy Points. The stored procedure allowed us to implement three separate advanced queries to create these three separate tables, and call it from the back-end at any point in time. As players and data is added to the database, the results of the stored procedure call will always be accurate to the current state of the database. Furthermore, we only needed to read from the database, with no need to manipulate data or write to the database. For that reason, a stored procedure allowed us the most seamless approach to implement our recommendation system. A transaction would have been unnecessary as we did not need to write to the database for this part of our application. We also implemented a simple trigger which allows the database to accurately keep track of the amount of players on each team. After any insertion, update, or deletion, the Player Count value for each affected team in the Teams table is incremented or decremented.
 
 
 
Dataflow 
 
Dataflow for adding player: 
 
A user will go to the homepage and will find a box which says Add Player: 

 
 
 
The user then types in the Player Name and the Team Name in the two boxes and will then click ‘Add Player’ 
 

 
 
 
 
Upon clicking on ‘Add Player’, the user will get redirected to the homepage page and if he scrolls down he will see the inserted player in the table: 
 

 
 
Dataflow for delete player:
 
Suppose the user wants to delete the player ‘Adam Stern’ that he just inserted. All he has to do is just click the trash can button under the Remove column on the row corresponding to ‘Adam Stern’ under the ‘Player Name’ column: 
 

 
Upon clicking the trash can for this row, the site will re-load the homepage with the table of players. As you can see the player ‘Adam Stern’ has been deleted and is no longer in the table: 

 
Dataflow for edit player: 
 
Suppose you want to change the player named ‘Adam Stern’ team from ARI to BOS. To do so, simply go to the homepage and find the row where Adam Stern is the player. Click on the pencil and pad icon under the ‘Edit’ column which will redirect to another page where you can enter the player’s new team: 
 

 
The page will look as follows: 
 

The user will then enter the new team’s abbreviation into the textbox where it says “Enter a valid abbreviation.” Enter the desired team’s abbreviation and then click ‘Update:’
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
From here, the user will then get redirected to the homepage and if he scrolls down, he can see that Adam Stern’s Team Name has changed from ARI to BOS. 
 
 
 
 
 
Data Flow for Search Player: 
 
Suppose the user wants to find the player ‘Adam Stern.’ To do this, simply go to the box where it says “Search for a Player”: 
 

 
Then, type in the name of the player and click the “Search” button:
 

 
 
 
 
 
 
 
 
 
The user will then get directed to the another page where it gives the search results: 
 
 
Data flow for the player and team recommendations: 
 
On the homepage the user will find a box that says “Click here to get the Team and Player Recommendations for MLB Fantasy Baseball” underneath the title: 
 

 
Upon clicking the button “Click Here” the user will get redirected to another page which will output the player recommendations by fantasy points, player recommendations by statistics for batters and pitchers, and team recommendations by fantasy points: 
 

 
 
 
 
 
 
 
Technical Challenge We Faced
 
The main technical challenge we encountered was struggling to connect our front-end and back-end. As we had very limited experience in web development prior to this project, this was our main point of contention. Originally, we attempted to use the Django framework to help support our backend code and integrate it with the HTML user interface; however, we were unable to run SQL queries within the Django-supported Python code. Furthermore, figuring out the routing between pages also proved to be quite difficult. In the end, we switched to Flask, which was a much more seamless integration with both the HTML and SQL queries.  
 
Did everything go according to plan?
 
While we did accomplish our main goal of creating a database of all MLB Players and a player recommendation system for users, we did not meet everything in our initial development plan. One big feature we wanted to add was to allow the user to filter through the database by setting various criteria, such as a minimum batting average or a maximum earned run average. This would give the user much more interaction with the database and allow a better understanding of a player’s performance. Our inability to reach this specification, along with our desired feature of a bracket predictor, was mainly driven by our inexperience with web development, and being able to have the back-end code work as expected with the user interface.


Division of Labor and Teamwork

	The division of labor worked where the team captain set a zoom meeting where all the team members met on a daily basis for a few hours. There was no particular assignment of roles as every member worked together on each of the tasks. If there was ever an issue where the output was not coming out properly or the code was not compiling, all team members would collectively do their own research on sites such as stackoverflow to get all of the code that is needed. The captain, however, was responsible for creating the initial base code for the team members to work with and so the team meetings were meant for scoping the project and debugging. Overall, the team worked well together and everyone contributed equally to each part through participating an equal amount during zoom meetings and there were no conflicts. 
