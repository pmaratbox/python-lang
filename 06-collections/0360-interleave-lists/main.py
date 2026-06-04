a = [1, 3, 5]
b = [2, 4, 6]
merged = [x for pair in zip(a, b) for x in pair]
print(" ".join(str(x) for x in merged))
