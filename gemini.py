import requests
from google import genai
import os


my_key = os.getenv('GEMINI_KEY')
client = genai.Client(api_key= my_key)

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

