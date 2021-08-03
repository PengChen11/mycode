#!/usr/bin/env python3

from deck import get_deck
from questions import question_color
from questions import question_suit
from questions import question_value
from game import win_game
from game import lose_game

def main():
    deck = get_deck()

    print(
    """

    Welcome to the game "Let me guess your card" ! In this this game, you will:
    1. Think about one Poker card in your mind (no Jokers).
    2. Answer the questions to let the AI guess what card is on your mind. AI will try 6 times to figure it out, or AI fails.
    3. Type in "exit" to quit the game at any time.

    Now let's begin...
    """
    )

    guessed_color = question_color()
    gussed_suit = None

    if guessed_color == 'red':
        gussed_suit = "heart" if question_suit("heart") == "yes" else "diamond"


    if guessed_color == 'black':
        gussed_suit = "spade" if question_suit("spade") == "yes" else "club"


    deck = [card for card in deck if card.suit == gussed_suit]

    round = 3
    current_value = 7
    high_value = 13
    low_value = 1

    print("\nNow let me guess the card value. Please consider J = 11, Q = 12, K = 13 and A = 1")

    while round <= 6:
        print(f"\nWe're at round {round} now! ")
        user_answer = question_value(current_value)

        if user_answer == "yes":

            low_value = current_value

            deck = [card for card in deck if card.value >= low_value and card.value <= high_value]

            if (len(deck) == 1):
                win_game(deck[0])
                quit()

            differ =(high_value - current_value) // 2

            current_value = (current_value + 1) if differ == 0 else (current_value + differ)
            round = round + 1

        else :
            high_value = current_value

            deck = [card for card in deck if card.value < current_value and card.value >= low_value]

            if (len(deck) == 1):
                win_game(deck[0])
                quit()

            differ =(high_value - low_value) // 2

            current_value =  (low_value + 1) if differ == 0 else (low_value + differ)

            round = round + 1


    lose_game(deck)


if __name__ == "__main__":
    main()
