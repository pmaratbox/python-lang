a = {1, 2, 3}
b = {2, 3, 4}
print(" ".join(str(x) for x in sorted(a | b)))
print(" ".join(str(x) for x in sorted(a & b)))
