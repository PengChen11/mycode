class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
     return f"{self.suit} {self.value}"

    def __repr__(self):
     return f"{self.suit} {self.value}"

def get_deck():

    suits = ['heart', 'diamond', 'spade', 'club']

    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

    return deck

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
