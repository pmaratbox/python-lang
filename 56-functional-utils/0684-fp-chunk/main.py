import more_itertools as mit

chunks = mit.chunked([1, 2, 3, 4, 5, 6], 2)
print("|".join(",".join(map(str, c)) for c in chunks))
