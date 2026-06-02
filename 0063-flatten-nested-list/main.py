nested = [[1, 2], [3, 4]]
flat = [x for row in nested for x in row]
print(" ".join(str(x) for x in flat))
