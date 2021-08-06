#!/usr/bin/env python3
from modules.settings import settings
from modules.questions import settings_question
from modules.questions import game_question
from termcolor import colored
import requests



def main():

    print(colored(f"\nWelcome to The Boring Game!! You'll be asked several trivia questions based on your specifications! \nIn the end you'll see your score! ", 'red'))
    url = "https://opentdb.com/api.php?"

    user_score = 0


    for key in settings:
        setting_value = settings_question(key, settings[key])
        if setting_value != None:
            url = url + f"&{key}={setting_value}"

    try:
        res = requests.get(url).json()
    except:
        print(colored('Sorry. something is wrong with the API server. They messed up, not me! ', 'red'))
        quit()

    if len(res["results"]) == 0:
        print(colored("\nSorry, we can't find any questions based on your specifications!", "red"))
        quit()


    for result in res["results"]:
        user_answer = game_question(result)
        if user_answer == result["correct_answer"]:
            user_score = user_score + 1

    final_score = round(user_score / len(res["results"]) * 100)

    print(f"\n {colored('Game Over !!', 'red')} You scored {colored(f'{final_score}', 'green')} / 100\n")


if __name__ == "__main__":
    main()
