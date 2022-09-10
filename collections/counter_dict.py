import collections
from collections import Counter


d = {'Молоток': 1, "Перчатки(пар)": 2, "Лопата": 3}
c = Counter(d)
print(c)
d1 = {'Молоток': 0 , "Лопата": 1, 'Газонокосилка': 1}
c.update(d1)
print(c)
lst = [f'Инструмент: {tool}, в количестве: {amount}' for tool in c.keys() for amount in c.values()]
print(lst)


ct = collections.Counter('ssadsaaabbb')
print(ct)