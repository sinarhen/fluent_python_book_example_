class Vector:

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, setter):
        self.__x = setter

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, setter):
        self.__y = setter

    def __iter__(self):
        return (i for i in (self.x, self.y))


