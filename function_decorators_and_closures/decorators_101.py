""" A decorator is a function that takes another function as its parameter (the target function)
and usually does some processing and returns a new function or the original"""


def deco(target):
    def inner():
        print('running inner function')
    return inner


@deco
def target():
    print('running target function')

