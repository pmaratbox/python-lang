matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]

for row in transposed:
    print(" ".join(str(x) for x in row))
