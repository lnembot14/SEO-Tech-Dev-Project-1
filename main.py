# import requests for APIs
import requests

response = requests.get(
    'https://api.balldontlie.io/fifa/worldcup/v1/teams',
    headers={'Authorization': 'c6a27bdd-ca76-4875-9b5b-b765a4e65ffa'}
)

teams = response.json()['data']
for team in teams:
    team_name = team['name']
    print(team_name)

#second API
response_2 = requests.get("https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds?regions=eu&markets=h2h,spreads,totals&oddsFormat=decimal&apiKey=3527d7d205521b10d613ced02cdface2")
betting_data = response_2.json()


# use http requests to get access to the JSON files from the odds/betting API and the players data API


# opening message - welcome user to app and ask them to enter a team name (condition for whether team is in world cup or not) or 


# move on to user being able to select players (1), schedule (2) and betting odds for most recent/latest game (3)

# based on option choosen
    # 1 - players 
        # list of players from team (numbered 1-n)
        # based on number selected players club team, age and other relevant stats
    # 2 - schedule
        # shows a list of teams games played and upcoming games 
    # 3 - betting odds
        # - returns teams odds from their most recent game (via FanDuel)

# navigation features
    # have a message to tell users whether they want to exit application completely or go back one step
        #- enter q to quit, enter b to go back 

# Nice to have: Gemini API integration