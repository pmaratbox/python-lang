import difflib

a = []
b = ["x", "y"]

sm = difflib.SequenceMatcher(None, a, b)
added = []
removed = []
equal = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("insert", "replace"):
        added += b[j1:j2]
    if tag in ("delete", "replace"):
        removed += a[i1:i2]
    if tag == "equal":
        equal += (i2 - i1)

print(len(added))
