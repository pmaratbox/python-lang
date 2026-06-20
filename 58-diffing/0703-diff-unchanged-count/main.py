import difflib

a = ["apple", "banana", "cherry"]
b = ["apple", "blueberry", "cherry", "date"]

sm = difflib.SequenceMatcher(None, a, b)
equal = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        equal += (i2 - i1)

print(equal)
