from pyrsistent import pset

# Persistent immutable set: adding an element RETURNS A NEW set,
# the original is left unchanged.
original = pset([1, 2, 3])
updated = original.add(4)

print(len(updated))   # new set has 4 elements
print(len(original))  # original unchanged: still 3 elements
