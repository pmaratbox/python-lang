from pyrsistent import pvector

# Persistent immutable list: setting an index RETURNS A NEW vector,
# the original is left unchanged.
original = pvector([1, 2, 3])
updated = original.set(0, 99)

print(" ".join(map(str, updated)))   # new list: 99 2 3
print(" ".join(map(str, original)))  # original unchanged: 1 2 3
