from pyrsistent import pvector

# Persistent immutable list: prepending and appending each
# RETURN A NEW vector; the original list is never mutated.
original = pvector([2, 3])
prepended = pvector([1]) + original   # add to the front -> new vector
final = prepended.append(4)           # add to the back  -> new vector

print(" ".join(map(str, final)))      # 1 2 3 4
