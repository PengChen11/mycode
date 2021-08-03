def question_color():
    while True:
        user_answer = input("\nIs this card \"red\" or \"black\"? or \"exit\" to quit the game.   ").strip().lower()
        if user_answer in ['red', 'black']:
            return user_answer
        if user_answer == 'exit':
            quit()
        else:
            print('\nBad input. Please answer \"red\" or \"black\"! or \"exit\" to quit the game.   ')

def question_suit(suit):
    while True:
        user_answer = input(f"\nIs this card a \"{suit}\"? or \"exit\" to quit the game.   ").strip().lower()
        if user_answer in ['yes', 'no']:
            return user_answer
        if user_answer == 'exit':
            quit()
        else:
            print('\nBad input. Please answer \"yes\" or \"no\"! or \"exit\" to quit the game.   ')

def question_value(value):
    while True:

        user_answer = input(f"\nIs this card value greater than or equal to {value}? or \"exit\" to quit the game.   ").strip().lower()
        if user_answer in ['yes', 'no']:
            return user_answer
        if user_answer == 'exit':
            quit()
        else:
            print('\nBad input. Please answer \"yes\" or \"no\"! or \"exit\" to quit the game.   ')
