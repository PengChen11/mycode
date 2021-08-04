from modules.deck import printed_card

def win_game(card):
    print_card = printed_card(card)
    print(f"\nBing go! I got it!! The card on your mind must be a {print_card} !!!\n")


def lose_game(deck):
    cards = []
    for card in deck:
        cards.append(printed_card(card))
    print(f"\nToo bad, I can't guess the card on your mind with in 5 rounds. But I think your card should be within {cards}\n")
