from inspect import getgeneratorstate


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print(f'-> coroutine {x}')


def simple_coro2(a):
    print('-> Started : a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received c =', c)


s = simple_coro2(14)
print(getgeneratorstate(s))
next(s)
print(getgeneratorstate(s))
s.send(28)
s.send(99)
print(getgeneratorstate(s))
