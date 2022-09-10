def old_chain(*args):
    for i in args:
        yield i


def chain(*args) -> list:  # -> for i in args: (for a in i == yield from i)
    i: object
    for i in args:
        yield from i


def older_chain(*args) -> list:
    a: object
    for i in args:
        for a in i:
            yield a


print(list(old_chain('ABC', range(1, 4))))
print(list(chain('ABC', range(1, 4))))
print(list(older_chain('ABC', range(1, 4))))
