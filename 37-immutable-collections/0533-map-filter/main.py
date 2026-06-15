from pyrsistent import pvector

# Persistent immutable list. Both filtering and mapping with .transform
# build and RETURN A NEW vector; the original is never mutated.
original = pvector([1, 2, 3, 4, 5])

# Keep even numbers, then multiply each survivor by 10.
evens = pvector(n for n in original if n % 2 == 0)
result = evens.transform([lambda i: True], lambda n: n * 10)

print(" ".join(map(str, result)))  # new list: 20 40
