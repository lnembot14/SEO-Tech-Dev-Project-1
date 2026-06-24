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
            return team["id"]
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

    

def liveSchedule():
    url = "https://api.football-data.org/v4/matches"

    headers = {
        "X-Auth-Token": my_api_key
    }

    response = requests.get(url, headers=headers)

    data = response.json()

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


def selectTeamPage():

    WCteams = worldCupTeams()

    print("Hello, welcome to the FIFA World Cup App!")

    while True:
        print("Please enter a team in the 2026 FIFA World Cup")
        userTeamSelection = input("Enter: ")

        teamID = findTeamId(userTeamSelection, WCteams)
        if teamID:
            print(f"You have selected {userTeamSelection}!, I.D: {teamID}")
            return teamID
        else:
            print("You have entered a team not in the 2026 FIFA World Cup")


def designatedTeamMenu(teamID):
    while True:
        print("===================== TEAM MENU =====================")
        print("1. View Players")
        print("2. View live Schedule")
        print("3. View Betting Odds")
        print("Or enter 'q' to quit")
        # print(4. Ask about the game using genai api)?

        userNumberSelection = input("Select an option (1 - 3): ")

        if userNumberSelection == "1":
            print("\n")
            listOfPlayers(teamID)
        
        elif userNumberSelection == "2":
            print("\n")
            liveSchedule()
    
        elif userNumberSelection == "3":
            print("coming soon")
            # add betting odds
        elif userNumberSelection == "q":
            print("You have chosen to quit the program. Goodbye!")
            break
        else:
            print("Whoops invalid option, enter a number (1,2, or 3)")

def main():
    team_id = selectTeamPage()
    designatedTeamMenu(team_id)

main()