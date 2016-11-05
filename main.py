from chapter1.card_deck import FrenchDeck, Card
from chapter1.utils import spades_high
from random import choice


def card_deck_container():
    deck = FrenchDeck()

    # methods we can use with __getitem__ implementation
    print(choice(deck))
    print(choice(deck))
    print(choice(deck), end='\n\n')

    print(deck[2:6], end='\n\n')

    for card in deck[:]:
        print(card)
    print(end='\n\n')

    # __contains__ is implicit because the class is a sequence type
    print(Card('Q', 'spades') in deck)

    for card in reversed(sorted(deck, key=spades_high)):
        print(card)


def execute_main():
    card_deck_container()


execute_main()

# fluent python where we left off => page 33
