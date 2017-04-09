"""the promotion decorator is used to register promotion functions within an array
so the best_promotion function can iterate over this array without the need for the
programmer to keep manually adding functions"""

promotion_registry = []


def promotion(promotion_function):
    promotion_registry.append(promotion_function)
    return promotion_function


@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    return order.total() * .07 if len(distinct_items) >= 10 else 0


def best_promo(order):
    return max(promo(order) for promo in promotion_registry)
