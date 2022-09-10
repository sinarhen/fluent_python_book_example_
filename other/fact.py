from sys import getsizeof


def fact(n):
    '''returns n'''
    return 1 if n < 2 else n*fact(n-1)


f = fact
mapp = list(map(fact, range(6)))
mapp1 = [fact(n) for n in range(6)]
