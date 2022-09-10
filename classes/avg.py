class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, *args):
        self.series = [x for x in args]
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(*args):
        series = [x for x in args]
        return sum(series) / len(series)
    return averager


avg = Averager()
print(avg(10, 20))

m = make_averager()
print(m(1, 5, 9, 13, 17))


def deco1(func):
    def wrapper():
        return func.__repr__
    return wrapper


@deco1
def deco():
    return 1


print(deco())

