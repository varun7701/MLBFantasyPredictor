"""Defines all the functions related to the database"""
from app import db
'''
def fetch_players() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Teams;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "PlayerName": result[0],
            "TeamName": result[1]
        }
        todo_list.append(item)

    return todo_list


def update_player_team(PlayerName: str, TeamName: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        PlayerName (str): Targeted Player
        TeamName (str): Updated TeamName

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Players set TeamName = "{}" where PlayerName = {};'.format(TeamName , PlayerName)
    conn.execute(query)
    conn.close()



def insert_new_player(PlayerName: str, TeamName: str) ->  str:
    """Insert new task to todo table.

    Args:
        PlayerName (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Insert Into Players (PlayerName, TeamName) VALUES ("{}", "{}");'.format(
        PlayerName, TeamName)
    conn.execute(query)
    conn.close()

    return PlayerName


def remove_player(PlayerName: str) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete FROM Players WHERE PlayerName={};'.format(PlayerName)
    conn.execute(query)
    conn.close()
'''