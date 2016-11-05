from chapter1.card_deck import FrenchDeck
from random import choice


def execute_main():
    deck = FrenchDeck()

    print(choice(deck))
    print(choice(deck))
    print(choice(deck))


execute_main()
