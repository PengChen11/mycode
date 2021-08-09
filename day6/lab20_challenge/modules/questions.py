from modules.settings import rovers_dict
from termcolor import colored

def rover_details(settings):

    index = 1
    for key in settings:
        print(f"{colored(index, 'red')}. {key}")
        index = index + 1

    while True:
        try:
            user_choice = int(input('Please choose a number: '))
            if user_choice >= 1 or user_choice <= len(settings):
                break;
            else:
                print('Bad choice. Please choose again.')
        except:
            print('Not a Number. Please choose again')
    return settings[user_choice]


def get_date():
    while True:
        try:
            user_choice = input('Please input an Earth data in yyyy-mm-dd format: ')
            break
        except:
            print('Not a Number. Please choose again')
    return user_choice
