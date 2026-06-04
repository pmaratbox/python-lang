first = [1, 2, 3, 4]
second = [2, 4]
remove = set(second)
result = [x for x in first if x not in remove]
print(" ".join(str(x) for x in result))
