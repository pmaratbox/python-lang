from pyrsistent import pvector

# Persistent immutable list: appending RETURNS A NEW vector,
# the original is left unchanged.
original = pvector([1, 2, 3])
updated = original.append(4)

print(" ".join(map(str, updated)))   # new list: 1 2 3 4
print(" ".join(map(str, original)))  # original unchanged: 1 2 3
