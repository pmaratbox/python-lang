from pyrsistent import pset

# Persistent immutable sets: .union() RETURNS A NEW pset,
# the originals are left unchanged.
a = pset([1, 2, 3])
b = pset([3, 4, 5])
union = a.union(b)

# Sort for deterministic output.
print(" ".join(map(str, sorted(union))))  # union: 1 2 3 4 5
