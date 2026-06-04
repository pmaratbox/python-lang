import itertools

data = [1, 2, 3, 4, 1]
result = list(itertools.takewhile(lambda x: x < 3, data))
print(" ".join(str(x) for x in result))
