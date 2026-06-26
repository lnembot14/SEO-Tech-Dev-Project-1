# import requests for APIs
import gemini
import betting
import wcFeaturesFunctions
import sys

# import for databases
import worldcup_database as db
from sqlalchemy import text
db.init_db()
db.buildTeamTable()

def end_app():
    db.clearFav()
    print("You have exited the program, enjoy the FIFA World Cup!")
    sys.exit()

def terminate_or_return(team_id, user_team):
    print("Enter 1 to go back to menu")
    print("Enter 2 to exit application")
    print("Enter 3 to choose a team/select new team")
    print("Enter 4 to keep exploring team\n")
    answer = int(input("Enter Selection: "))
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
    print("========================== USER SELECTION ========================== ")
    user_team = str(input("Hello, please choose a team to begin: "))
    WCTeams = wcFeaturesFunctions.worldCupTeams()
    teamID = wcFeaturesFunctions.findTeamId(user_team, WCTeams)
    if teamID:
        return teamID
    else:
        print("Team not in world cup")

def get_schedule():
    wcFeaturesFunctions.liveSchedule()
    print("1. Back to Menu\n2. Exit Program\n")
    next_step = int(input("Enter Selection: "))
    if next_step == 1:
        next_action = welcome_page()
        if next_action == 1:
            wcFeaturesFunctions.liveSchedule()
        elif next_action == 2:
            t_id, t_name = selection_team()
            menu_selection(t_id, t_name)
    elif next_step == 2:
        end_app()



def welcome_page():
    print("========================== Hello welcome to the FIFA World Cup App! ========================== ")
    first_choice = int(input("1. Select option one to view live FIFA World Cup Schedule\n2. Select option two to choose team\nPlease enter a option: "))
    return first_choice


def menu_selection(id_team, user_team):
    while True:
        print("\n========================== Menu ==========================\n1. Players \n2. Overview\n3. Odds\n4. Fun Fact\n5. Claim Your Favorite Team\n6. Exit Application \n==========================================================")

        user_choice = int(input("Enter Selection: "))

        if user_choice == 1 :
            wcFeaturesFunctions.listOfPlayers(id_team)
    
            print(f"\n=========================================================================================\n")
            terminate_or_return(id_team, user_team)
        elif user_choice == 2:
            gemini.overview_response(user_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 3 :
            print("================MONEYLINE============")
            print(betting.betting_odds(user_team))
            print("=====================================")
            terminate_or_return(id_team, user_team)
        elif user_choice == 4:
            gemini.fun_fact_team(user_team)
            terminate_or_return(id_team, user_team)
        elif user_choice == 5:
            favTeamId = id_team
            db.saveFav(favTeamId)
            print(f"{user_team} saved as your favorite team")
            result = db.getFav()
            if result:
                print("===================== FAVORITE TEAM =====================")
                print(f"Team: {result[0]}")
                print(f"Coach: {result[1]}")
                print(f"Colors: {result[2]}")
                print(f"Founded: {result[3]}")
            else:
                print("did not save properly")
        elif user_choice == 6:
            end_app()
        else:
            print("You have entered invalid choice")
            end_app()

def main():
    start_val = welcome_page()
    if start_val == 1:
        get_schedule()
    elif start_val == 2:
        team_id, team_name = selection_team()
        menu_selection(team_id, team_name)
    elif start_val == 3:

            result = db.getFav()

            if result:
                print("===================== FAVORITE TEAM =====================")
                print(f"Team: {result[0]}")
                print(f"Coach: {result[1]}")
                print(f"Colors: {result[2]}")
                print(f"Founded: {result[3]}")
            else:
                print("No favorite team yet selected")
    

main()
