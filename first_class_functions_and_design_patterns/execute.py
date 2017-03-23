from first_class_functions_and_design_patterns.classic_strategy_pattern import *


def execute():

    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]

    print(Order(joe, cart, FidelityPromotion()))
    print(Order(ann, cart, FidelityPromotion()))


execute()