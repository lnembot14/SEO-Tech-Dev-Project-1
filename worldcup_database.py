import requests
import os
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, text

engine = sa.create_engine("sqlite:///worldcup_2.db")


def init_db():
    with engine.begin() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, team_id INTEGER)"))
        

def buildTeamTable():

    my_api_key = os.getenv('SOCCER_APIKEY')


    url = "http://api.football-data.org/v4/competitions/WC/teams"
    headers = {
        "X-Auth-Token": my_api_key
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    teams = []

    for team in data["teams"]:

        teams.append({
            "team_id": team["id"],
            "team_name": team["name"],
            "coach": team["coach"]["name"],
            "club_colors": team["clubColors"],
            "tla": team["tla"],
            "founded": team["founded"]
        })

    worldcup_2 = pd.DataFrame(teams)

    worldcup_2.to_sql("teamInfo", con=engine, if_exists="replace", index=False)

def saveFav(team_id):
        with engine.begin() as connection:
            connection.execute(text("DELETE FROM favorites"))

            connection.execute(text("INSERT INTO favorites (team_id) VALUES (:team_id)"),{"team_id": team_id})
           

def getFav():
        with engine.begin() as connection:
            result = connection.execute(text("SELECT t.team_name, t.coach, t.club_colors, t.founded FROM teamInfo t JOIN favorites f ON t.team_id = f.team_id")).fetchone()

            return result

def clearFav():
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM favorites"))
        