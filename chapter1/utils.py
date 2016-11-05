from .card_deck import FrenchDeck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """Card sorting function"""

    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
