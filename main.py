# import requests for APIs
import gemini
import betting
import wcFeaturesFunctions
import sys


def end_app():
    return sys.exit()

def terminate_or_return(team_id, user_team):
    print("Enter 1 to go back to menu")
    print("Enter 2 to exit application")
    print("Enter 3 to choose a team/select new team")
    print("Enter 4 to keep exploring team")
    answer = int(input(""))
    if answer == 1:
        result = welcome_page()
        if result == 1:
            get_schedule()
        elif result == 2:
            val1, val2 = selection_team()
            menu_selection(val1, val2)
    elif answer == 2:
        end_app()
    elif answer == 3:
        t1, t2= selection_team()
        menu_selection(t1, t2)
    elif answer == 4:
        menu_selection(team_id, user_team)



def selection_team():
    user_team = str(input("Hello, please choose a team to begin: "))
    WCTeams = wcFeaturesFunctions.worldCupTeams()
    teamID = wcFeaturesFunctions.findTeamId(user_team, WCTeams)
    if teamID:
        return teamID
    else:
        print("Team not in world cup")

def get_schedule():
    wcFeaturesFunctions.liveSchedule()
    next_step = int(input("1. Back to Menu\n2. Exit Progran\n"))
    if next_step == 1:
        next_action = welcome_page()
        if next_action == 1:
            wcFeaturesFunctions.liveSchedule()
        elif next_action == 2:
            t_id, t_name = selection_team()
            menu_selection(t_id, t_name)
    elif next_step == 2:
        sys.exit()



def welcome_page():
    print("Hello welcome to the FIFA World Cup App!")
    first_choice = int(input("1. Select option one to view live FIFA World Cup Schedule\n2. Select option two to choose team\n"))
    return first_choice


def menu_selection(id_team, user_team):
    while True:
        print("Menu\n1. Players \n2. Overview\n3. Odds\n4. Fun Fact\n5. Exit Application \n")

        user_choice = int(input("Enter Selection: "))

        if user_choice == 1 :
            wcFeaturesFunctions.listOfPlayers(id_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 2:
            gemini.overview_response(user_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 3 :
            betting.betting_odds(user_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 4:
            gemini.fun_fact_team(user_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 5:
            end_app()
        else:
            print("You have entered invalid choice")



def main():
    start_val = welcome_page()
    if start_val == 1:
        get_schedule()
    elif start_val == 2:
        team_id, team_name = selection_team()
        menu_selection(team_id, team_name)

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
