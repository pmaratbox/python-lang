import more_itertools as mit

pairs = mit.zip_broadcast([1, 2, 3], ["a", "b", "c"])
print(",".join(f"{n}{s}" for n, s in pairs))
