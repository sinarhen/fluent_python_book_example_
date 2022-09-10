from functools import partial
from operator import mul


triple = partial(lambda x,y: x * y, n)
print(triple(10))