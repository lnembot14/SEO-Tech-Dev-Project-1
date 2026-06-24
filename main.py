# import requests for APIs
import requests

response_2 = requests.get("https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds?regions=eu&markets=h2h,spreads,totals&oddsFormat=decimal&apiKey=3527d7d205521b10d613ced02cdface2")
betting_json = response_2.json()

world_cup_teams = [
    "Argentina",
    "Australia",
    "Austria",
    "Belgium",
    "Bosnia and Herzegovina",
    "Brazil",
    "Canada",
    "Cape Verde",
    "Colombia",
    "Croatia",
    "Curacao",
    "Czechia",
    "DR Congo",
    "Ecuador",
    "Egypt",
    "England",
    "France",
    "Germany",
    "Ghana",
    "Haiti",
    "Iran",
    "Iraq",
    "Ivory Coast",
    "Japan",
    "Jordan",
    "Mexico",
    "Morocco",
    "Netherlands",
    "New Zealand",
    "Norway",
    "Panama",
    "Paraguay",
    "Portugal",
    "Qatar",
    "Saudi Arabia",
    "Scotland",
    "Senegal",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Tunisia",
    "Turkey",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Algeria"
]

user_team = str(input("Hello, please choose a team to begin: "))


if user_team in world_cup_teams:
    print("Great let's fetch this teams next opponent where you can check out the teams moneyline odds for the next game via Pinnacle")
    for game in betting_json:
        if user_team == game['home_team'] or user_team == game['away_team']:
            for bet_platform in game['bookmakers']:
                if bet_platform['title'] == 'Pinnacle':
                    for outcome in bet_platform['markets']:
                        if outcome['key'] == 'h2h':
                            h2h_dict = {}
                            for moneyline in outcome['outcomes']:
                                h2h_dict[moneyline['name']] = moneyline['price']
                            list_of_odds = []
                            for key, value in h2h_dict.items():
                                list_of_odds.append(f"{key} {value}")
                            final_format = " | ".join(list_of_odds)
                            print(f"Moneyline for next match: {final_format}")
            
    



# use http requests to get access to the JSON files from the odds/betting API and the players data API



# opening message - welcome user to app and ask them to enter a team name (condition for whether team is in world cup or not)
#  or 

    


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