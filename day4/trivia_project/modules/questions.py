import random
from termcolor import colored

def settings_question(setting, valid_selections_dict):

    key_list = list(valid_selections_dict.keys())

    print(colored(f"\nPlease select { 'number of questions' if setting == 'amount' else setting} : ", "green"))

    index = 1
    for selection in valid_selections_dict:
        print(f"{colored(index, 'red')}. {selection}")
        index = index + 1

    answer = -1
    while answer > len(valid_selections_dict) or answer <0:
        try:
            answer = int(input("(enter a number here, or 0 to exit at any time):  "))
        except:
            print(colored('NOT a number, please select again! ', 'red'))
    choosed_key = key_list[answer - 2]

    if answer == 0:
        quit()

    if answer == 1 and setting == 'amount':
        return valid_selections_dict[key_list[answer - 1]]

    return valid_selections_dict[choosed_key] if answer != 1 else None


def game_question(question_dict):
    question = question_dict["question"]

    answer_pool = question_dict["incorrect_answers"]
    answer_pool.append(question_dict["correct_answer"])

    random.shuffle(answer_pool)

    print(colored(f"\nQuestion: {question} ", "yellow") )
    print(colored("\nPlease choose one from the following answers: ", "green"))

    index = 1
    for answer in answer_pool:
        print(f"{colored(index, 'red')}. {answer}")
        index = index + 1

    user_answer = -1
    while user_answer > len(answer_pool) or user_answer < 0:
        try:
            user_answer = int(input("\n(enter a number here, or 0 to exit at any time):  "))
        except:
            print(colored('\nNOT a number, please select again! ', 'red'))

    if user_answer == 0:
        quit()

    return answer_pool[user_answer - 1]

