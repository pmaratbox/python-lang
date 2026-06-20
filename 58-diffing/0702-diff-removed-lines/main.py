import difflib

a = ["apple", "banana", "cherry"]
b = ["apple", "blueberry", "cherry", "date"]

sm = difflib.SequenceMatcher(None, a, b)
removed = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("delete", "replace"):
        removed += a[i1:i2]

print(",".join(removed))
