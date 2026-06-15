from pyrsistent import pmap, m

original = m(user=m(age=30))
updated = original.transform(["user", "age"], 31)

print(updated["user"]["age"])
print(original["user"]["age"])
