def gen():
    yield from 'AB'
    yield from range(1, 3)

print(list(gen()))