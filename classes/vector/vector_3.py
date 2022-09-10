from array import array
import math


class Vector:
    TYPECODE = 'd'

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
        self._components = []

    def __bytes__(self):
        return bytes([ord(self.TYPECODE)]) + bytes(array(self.TYPECODE, self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x},{self.y})'

    def __hash__(self):
        hashes = (hash(i) for i in self._components)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
