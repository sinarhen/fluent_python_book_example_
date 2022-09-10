from functools import reduce
from operator import mul, itemgetter
from random import randint


def fact(n):
    return reduce(mul, range(1, n + 1))


print(fact(10))


metro_data = {
    ('Tokyo', '10000000'),
    ('Brazil', '56000000'),
    ('Singapore', '100000000'),

}


for item in sorted(metro_data, key=itemgetter(1)):
    print(item)


cc = itemgetter(0, 1)
for city in metro_data:
    print(cc(city))
