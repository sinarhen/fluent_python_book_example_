promos = []


def deco(func):
    promos.append(func())
    return func


@deco
def one():
    return 1


@deco
def two():
    return 2


@deco
def three():
    return 3


def func(a):
    global b
    print(a)
    b = 9
    print(b)


func(2)
print(promos)
