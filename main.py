# import requests for APIs
import gemini
import betting

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
