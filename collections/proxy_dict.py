from types import MappingProxyType


d = {1: 'A'}
d_proxy = MappingProxyType(d)
d[2] = 'Б'

print(d, d_proxy, end=" ")