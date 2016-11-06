# tuple unpacking * used to grab excess items
a, b, *rest = range(5)
# >>> (0, 1, [2, 3, 4])

# In the context of parallel assignment, the * prefix can be applied to exactly one variable,
# but it can appear in any position:
# >>> a, *body, c, d = range(5)
# >>> a, body, c, d
# (0, [1, 2], 3, 4)
# >>> *head, b, c, d = range(5)
# >>> head, b, c, d
# ([0, 1], 2, 3, 4)

pass
