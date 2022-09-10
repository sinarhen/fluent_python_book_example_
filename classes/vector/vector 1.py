from array import array
import math


class Vector:
    TYPECODE = 'd'

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __bytes__(self):
        return bytes([ord(self.TYPECODE)]) + bytes(array(self.TYPECODE, self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x},{self.y})'

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets)
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)


v1 = Vector(3, 4)
print(v1.x, v1.y)
print(bytes(v1))
