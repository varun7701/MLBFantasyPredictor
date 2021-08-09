""" Specifies routing for the application"""
'''
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<str:PlayerName>", methods=['POST'])
def delete(PlayerName):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_player(PlayerName)
        result = {'success': True, 'response': 'Removed player'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<str:PlayerName>", methods=['POST'])
def update(PlayerName):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "TeamName" in data:
            db_helper.update_player_team(PlayerName, data["TeamName"])
            result = {'success': True, 'response': 'Team Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_player(data['TeamName'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    players = db_helper.fetch_players()
    return render_template("index.html", Players=players)
'''