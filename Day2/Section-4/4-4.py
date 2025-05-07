from itertools import count, cycle,  repeat, chain, islice, tee, groupby, permutations, combinations
from operator import itemgetter
# 1. count()
id_gen = count(1)
print(next(id_gen))  # 1
print(next(id_gen))  # 2
print(next(id_gen))  # 3

# 2. cycle()

colors = cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors), end=' ')

# 3. repeat() – Duplicate Values

nones = list(repeat(None, 10))
print(nones)

# 4. chain() – Flatten Multiple Lists
flattened = list(chain([1, 2], [3, 4], [5]))
print(flattened)  # [1, 2, 3, 4, 5]

# 5. islice()
sliced = list(islice(range(10), 3, 7))
print(sliced)  # [3, 4, 5, 6]

# 6. tee()
numbers = iter([1, 2, 3, 4])
a, b = tee(numbers)

print(list(a))  # [1, 2, 3, 4]
print(list(b))  # [1, 2, 3, 4]

# 7. groupby()

data = [
    {"type": "fruit", "name": "apple"},
    {"type": "fruit", "name": "banana"},
    {"type": "veg", "name": "carrot"},
    {"type": "veg", "name": "broccoli"}
]

# Must be sorted by the key!
data.sort(key=itemgetter("type"))

for key, group in groupby(data, key=itemgetter("type")):
    print(key, list(group))
# fruit [{'type': 'fruit', ...}]
# veg [{'type': 'veg', ...}]


# 8. permutations() and combinations()
items = [1, 2, 3]

print("Permutations (pairs):", list(permutations(items, 2)))
# [(1, 2), (1, 3), (2, 1), ...]

print("Combinations (triples):", list(combinations(items, 3)))
# [(1, 2, 3)]
