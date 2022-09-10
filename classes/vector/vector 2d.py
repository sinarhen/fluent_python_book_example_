
class Vector:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)


# __slots__ is optimizing and limiting amount of attrs in class
class Vector1:
    __slots__ = ('__x', '__y')
