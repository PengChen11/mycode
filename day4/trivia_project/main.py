#!/usr/bin/env python3
from modules.settings import settings
from modules.questions import settings_question
from modules.questions import game_question

import requests

def main():

    print("\nWelcome to The Boring Game!! You'll be asked several trivia questions based on your specifications! In the end you'll see your score! ")
    url = "https://opentdb.com/api.php?"

    user_score = 0


    for key in settings:
        setting_value = settings_question(key, settings[key])
        if setting_value != 0:
            url = url + f"&{key}={setting_value}"

    res = requests.get(url).json()

    for result in res["results"]:
        user_answer = game_question(result)
        if user_answer == result["correct_answer"]:
            user_score = user_score + 1

    final_score = round(user_score / len(res["results"]) * 100)

    print(f"\n Game Over !! You scored {final_score} / 100")


if __name__ == "__main__":
    main()
