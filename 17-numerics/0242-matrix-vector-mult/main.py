m = [[1, 2], [3, 4]]
v = [5, 6]
result = [sum(a * b for a, b in zip(row, v)) for row in m]
print("{} {}".format(*result))
