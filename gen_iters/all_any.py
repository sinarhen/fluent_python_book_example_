import random


lst1 = [1, 2, 3, 6]
lst2 = [10, 11]
print(any(sign in lst1 for sign in lst2))


def d6():
    return random.randint(1, 6)


d6_iter = iter(d6, 2)
for roll in d6_iter:
    print(roll)

