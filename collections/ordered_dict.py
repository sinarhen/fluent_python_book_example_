from collections import OrderedDict, ChainMap


a = {1: '1', 2: '2'}
b = {2: '2', 1: '1'}

order1 = OrderedDict(a)
order2 = OrderedDict(b)

print(a == b)
print(order1 == order2)


chain = ChainMap(a, b)
print(chain)