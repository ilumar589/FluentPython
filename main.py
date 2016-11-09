from chapter1.card_deck import FrenchDeck, Card
from chapter1.utils import spades_high
from chapter1.vector_n import Vector
from random import choice
from array import array


def list_comprehensions_vs_generator_expressions():
    """To initialize tuples, arrays and other types of sequences, you could also start from a
       list compositions but a generator expression saves memory because it yields items one by one using the iterator
       protocol instead of building a whole list just to feed another constructor.

       Genexps use the same syntax as listcomps, but are enclosed in parenthesis rather than
       brackets.
    """
    # list comprehension
    colors = ['white', 'black']
    sizes = ['S', 'M', 'L']

    t_shirts = [(color, size) for color in colors for size in sizes]

    print(t_shirts)

    # generator expressions
    symbols = '%^&!#*$'

    # basically tuple() function accepts a generator expression to create a tuple instance
    # with data from the expression
    # here the enclosing parenthesis are not necessary because it's the only argument in the tuple function
    print(tuple(ord(s) for s in symbols))

    # here the enclosing parenthesis are necessary
    # array.array is a flat sequence object instance and the first parameter
    # is the type of data contained ; ex: I - signed integers
    print(array('I', (ord(s) for s in symbols)))

    # feeds the for loop one by one, not storing a list in memory
    for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(t_shirt)


def vector_container():
    print(repr(Vector(1, 2)), )
    print(Vector(1, 2) + Vector(2, 4))
    print(Vector(3, 5) * 6)


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
    # card_deck_container()
    # vector_container()

    list_comprehensions_vs_generator_expressions()

execute_main()

# fluent python where we left off => page 47 => Slicing
