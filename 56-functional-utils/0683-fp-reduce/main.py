from functools import reduce

print(reduce(lambda a, b: a + b, range(1, 6), 0))
