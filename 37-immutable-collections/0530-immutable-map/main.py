from pyrsistent import pmap

original = pmap({"a": 1})
updated = original.set("b", 2)

print(" ".join(sorted(updated.keys())))
print(" ".join(sorted(original.keys())))
