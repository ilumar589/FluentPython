from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):

        # unpack tuple or enumerate values
        # this will be packed back in inside
        # the format function and iterated over
        return str.format('Vector({0}, {1})', *(self.x, self.y))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """Vector instance * value is allowed.

        But value * vector instance is not allowed
        which violates the commutative property
        __rmul__ must be implemented (Chapter 13)
        """
        return Vector(self.x * scalar, self.y * scalar)
