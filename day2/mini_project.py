class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
     return f"{self.suit} {self.value}"

    def __repr__(self):
     return f"{self.suit} {self.value}"

suits = ['heart', 'diamond', 'spade', 'club']

deck = [Card(value, suit) for value in range(1, 14) for suit in suits]


def printed_card(card):
    print_value = card.value
    if card.value == 1:
        print_value = "A"
    elif card.value == 11:
        print_value = "J"
    elif card.value == 12:
        print_value = "Q"
    elif card.value == 13:
        print_value = "K"
    return Card(print_value, card.suit)


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

def win_game(card):
    print_card = printed_card(card)
    print(f"\nBing go! I got it!! The card on your mind must be {print_card} !!!")

def lose_game(deck):

    cards = []
    for card in deck:
        cards.append(printed_card(card))
    print(f"Too bad, I can't guess the card on your mind with in 5 rounds. But I think your card should be within {cards}")



print(
"""

Welcome to the game "let me guess your card" ! In this this game, you will:
1. Think about one poker card in your mind (no Jokers).
2. Anwer the questions to let the AI guess what card is on your mind. AI will try it 6 times to guess it, or AI fails.

Now let's begin...
"""
)

guessed_color = question_color()
gussed_suit = None

if guessed_color == 'red':
    deck = [card for card in deck if card.suit == 'heart' or card.suit == 'diamond']
    gussed_suit = "heart" if question_suit("heart") == "yes" else "diamond"


if guessed_color == 'black':
    deck = [card for card in deck if card.suit == 'spade' or card.suit == 'club']
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


