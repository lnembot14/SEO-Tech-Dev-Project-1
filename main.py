# import requests for APIs
import requests
from google import genai
import sys
import os


response_2 = requests.get("https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds?regions=eu&markets=h2h,spreads,totals&oddsFormat=decimal&apiKey=8549f0c11606067fdb19f4c7134e43d8")
betting_json = response_2.json()

my_key = os.getenv('GEMINI_KEY')
client = genai.Client(api_key= my_key)

world_cup_teams = [
    "Argentina","Australia","Austria","Belgium","Bosnia and Herzegovina","Brazil","Canada","Cape Verde","Colombia","Croatia","Curacao","Czechia",
    "DR Congo","Ecuador","Egypt","England","France","Germany","Ghana","Haiti","Iran","Iraq","Ivory Coast","Japan","Jordan","Mexico","Morocco",
    "Netherlands","New Zealand","Norway","Panama","Paraguay","Portugal","Qatar","Saudi Arabia","Scotland","Senegal","South Africa","South Korea","Spain","Sweden",
    "Switzerland","Tunisia","Turkey","United States","Uruguay","Uzbekistan","Algeria"
]

def end_app():
    print("You have excited the program, goodbye!")
    sys.exit()

def terminate_or_return():
    print("Enter 1 to go back to main menu ")
    print("Enter 2 to exit application")
    print("Enter 3 to choose new Team")
    answer = int(input(""))
    if answer == 1:
        pass
    elif answer == 2:
        end_app()
    elif answer == 3:
        new_team = select_team_page()
        menu_selection(new_team)


def betting_odds(team):
    print("Great let's fetch this teams next opponent where you can check out the teams moneyline odds for the next game via Pinnacle")
    for game in betting_json:
            if team == game['home_team'] or team == game['away_team']:
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
                                print(f"================{team.upper()} ODDS===========================")
                                print(f"Moneyline for next match: {final_format}")
                                print("===============================================================")
    terminate_or_return()

def overview_response(team):
    gen_ai_response2 = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    config={
        "system_instruction": "Your an all knower of everything World Cup and have to give a brief overview of a specific team in the competition for someone who doesn't know that much about soccer"
    },
    contents=f"Give me a brief overview of {team} and anything else that is relevant, make sure to keep it nice and sweet include star players past and present, exclude fun fact "
    )
    overview = gen_ai_response2.text
    print(f"================== {team.upper()} OVERVIEW =========================")
    print(overview)
    print("=====================================================================")
    terminate_or_return()

def fun_fact_team(teamName):
    print("Generating your fun fact...")
    gen_ai_response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    config={
        "system_instruction": "Act as if you're an expert on all things World Cup, keep your answers nice and brief"
    },
    contents=f"Give me a fun fact about the following team {teamName}"
    )
    fun_fact = gen_ai_response.text
    print(f"================= {teamName.upper()} FUN FACT==========================")
    print(fun_fact)
    print("===================================================================")
    terminate_or_return()

def select_team_page():
    print("Hello welcome to the FIFA World Cup App!")
    user_team = str(input("Hello, please choose a team to begin: "))
    if user_team not in world_cup_teams:
        print("Team is not in WC, try again!")
    else:
        return user_team
        


def menu_selection(user_team):
    while True:
        print("Menu\n1. Players \n2. Overview\n3. Odds\n4. Schedule\n5. Fun Fact\n6. Exit Application\n")

        user_choice = int(input("Enter Selection: "))

        if user_choice == 1 :
            print("Coming soon")
        elif user_choice == 2:
            overview_response(user_team)
        elif user_choice == 3 :
            betting_odds(user_team)
        elif user_choice == 4:
            print("Coming soon")
        elif user_choice == 5:
            fun_fact_team(user_team)
        elif user_choice == 6:
            print("You have excited the program, goodbye!")
            break
        else:
            print("You have entered invalid choice")



def main():
    team = select_team_page()
    menu_selection(team)

main()
    
            
    



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