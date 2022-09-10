from itertools import repeat, cycle, combinations_with_replacement, permutations, groupby

# a = repeat(1, 2)
# for i in a:
#     print(i)

# cy = cycle('ABC')
# next(cy)
# ic = islice(cy, 7)
# print(list(ic))


# a = list(permutations('ABC', 2))
# print(sorted(a, key=lambda x: x))

# animals = ['dolphin', 'rat', 'bat', 'giraffe', 'bear', 'fish', 'lion', 'zebra']
# gr_animals = groupby(animals, len)
# for length, group in gr_animals:
#     print(f'{length} -> {list(group)}')
#
chars = 'LLLGGGGAAAFFF'
gr_chars = groupby(chars)
for char, group in gr_chars:
    print(f'{char} -> {list(group)}, length={len(list(group))}')
