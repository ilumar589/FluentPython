import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Deck of cards class"""

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds club hearts'.split()

    # even though ranks and suits are class variables and are shared between all instances
    # they are still references with self.variable name
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    # implementing this method let's us use stuff like
    # len(instance) and we get the number of cards in our deck
    def __len__(self):
        return len(self._cards)

    # because this method is implemented the python interpreter
    # uses it in varied situations. For example this class is now
    # considered a sequence and we can use syntax like instance[0]
    # and we would get the first card or something cooler like
    # random.choice(instance) and we can get random cards
    # and even cooler the instances of this class auto-magically
    # support slicing now instance[1:n]
    def __getitem__(self, position):
        return self._cards[position]
