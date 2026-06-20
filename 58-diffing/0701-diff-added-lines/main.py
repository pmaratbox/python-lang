import difflib

a = ["apple", "banana", "cherry"]
b = ["apple", "blueberry", "cherry", "date"]

sm = difflib.SequenceMatcher(None, a, b)
added = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("insert", "replace"):
        added += b[j1:j2]

print(",".join(added))
