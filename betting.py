import requests

response_2 = requests.get("https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds?regions=eu&markets=h2h,spreads,totals&oddsFormat=decimal&apiKey=dc8a3b195dba38336c9c5b0f50cdad8e")
betting_json = response_2.json()


def betting_odds(team):
    found = False
    for game in betting_json:
            if team == game['home_team'] or team == game['away_team']:
                found = True
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
    if not found:
        return "Team has played their final group stage match, no odds available"

print(betting_odds("Brazil"))