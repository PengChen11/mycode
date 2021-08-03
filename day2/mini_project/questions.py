def question_color():
    while True:
        user_answer = input("\nIs this card red or black?").strip().lower()
        if user_answer in ['red', 'black']:
            return user_answer
        else:
            print('\nBad input. Please answer red or black!')

def question_suit(suit):
    while True:
        user_answer = input(f"\nIs this card a {suit}?").strip().lower()
        if user_answer in ['yes', 'no']:
            return user_answer
        else:
            print('\nBad input. Please answer yes or no!')

def question_value(value):
    while True:

        user_answer = input(f"\nIs this card value greater than or equal to {value}?").strip().lower()
        if user_answer in ['yes', 'no']:
            return user_answer
        else:
            print('\nBad input. Please answer yes or no!')
