import random

def settings_question(setting, valid_selections_dict):

    key_list = list(valid_selections_dict.keys())

    print(f"\nPlease select { 'number of questions' if setting == 'amount' else setting} : ")

    index = 1
    for selection in valid_selections_dict:
        print(f"{index}. {selection}")
        index = index + 1

    answer = -1
    while answer > len(valid_selections_dict) or answer <0:
        try:
            answer = int(input("(enter a number here, or 0 to exit at any time):  "))
        except:
            print('NOT a number, please select again! ')
    choosed_key = key_list[answer - 1]

    if answer == 0:
        quit()

    return valid_selections_dict[choosed_key]


def game_question(question_dict):
    question = question_dict["question"]

    answer_pool = []
    answer_pool.append(question_dict["correct_answer"])

    for answer in question_dict["incorrect_answers"]:
        answer_pool.append(answer)

    random.shuffle(answer_pool)

    print(f"\nQuestion: {question} ")
    print("\nPlease choose one from the following answers: ")
    index = 1
    for answer in answer_pool:
        print(f"{index}. {answer}")
        index = index + 1

    user_answer = -1
    while user_answer > len(answer_pool) or user_answer < 0:
        try:
            user_answer = int(input("\n(enter a number here, or 0 to exit at any time):  "))
        except:
            print('\nNOT a number, please select again! ')

    if user_answer == 0:
        quit()

    return answer_pool[user_answer - 1]

