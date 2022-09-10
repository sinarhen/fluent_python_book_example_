import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Унесенные ветром")


ender = weakref.finalize(s1, bye)

""">>>ender.alive
True
>>>bye
<function bye at 0x000002079B31A830>
>>>ender
<finalize object at 0x20798243ca0; for 'set' at 0x2079b1ee500>
>>>del s1
>>>ender.alive
True
>>>ender
<finalize object at 0x20798243ca0; for 'set' at 0x2079b1ee500>
>>>s2 = 'spam'
Унесенные ветром
>>>ender.alive
False"""