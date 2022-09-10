class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x},{self.y})'


v1 = Vector(1, 2)
v2 = Vector(1, 3)
print(v1+v2)
