import difflib

a = ["apple", "banana", "cherry"]
b = ["apple", "banana", "cherry"]

sm = difflib.SequenceMatcher(None, a, b)
added = []
removed = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("insert", "replace"):
        added += b[j1:j2]
    if tag in ("delete", "replace"):
        removed += a[i1:i2]

print(f"{len(added)} {len(removed)}")
