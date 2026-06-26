import os
import requests
import json

# Global Variable
my_api_key = os.getenv('SOCCER_APIKEY')


def worldCupTeams():
    url = "http://api.football-data.org/v4/competitions/WC/teams"

    headers = {
        "X-Auth-Token": my_api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["teams"]

def findTeamId(teamName, teams):
    for team in teams:
        if teamName.lower() == team["name"].lower():
            return team["id"], team["name"]
    return None


def listOfPlayers(id):
    url =  f"http://api.football-data.org/v4/teams/{id}"
    headers = {
        "X-Auth-Token": my_api_key
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    squad = data["squad"]

    print(f"==================================== List of Players ====================================\n")
    for i, person in enumerate(squad, start = 1):
        print(f"{i}. Player: {person['name']:<25} | Position: {person['position']:<15} | Nationality: {person['nationality']}")

    return squad

# Add playerSelect() function
    

def liveSchedule():
    url = "https://api.football-data.org/v4/matches"

    headers = {
        "X-Auth-Token": my_api_key
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    print("============================================================================================")
    for match in data["matches"]:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        match_date = match["utcDate"]
        status = match["status"]
        home_score = match["score"]["fullTime"]["home"]
        away_score = match["score"]["fullTime"]["away"]

        print(f"Date: {match_date}")
        print(f"Match: {home_team} vs {away_team}")
        print(f"Status: {status}")

        print(f"Score: {home_team} {home_score} - {away_score} {away_team}")

        print("-----------------------------------------------------------------------------------------")
    print("============================================================================================")
