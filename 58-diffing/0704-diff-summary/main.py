import difflib

# Two fixed line-lists. Diff A -> B with the stdlib difflib SequenceMatcher,
# whose opcodes are LCS-determined (deterministic, independent of how the edit
# script is ordered). A CHANGE/replace delta maps to removed(source)+added(target).
a = ["apple", "banana", "cherry"]
b = ["apple", "blueberry", "cherry", "date"]

sm = difflib.SequenceMatcher(None, a, b)
added = []
removed = []
unchanged = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("insert", "replace"):
        added += b[j1:j2]
    if tag in ("delete", "replace"):
        removed += a[i1:i2]
    if tag == "equal":
        unchanged += (i2 - i1)

# Print "<added> <removed> <unchanged>" counts, space-joined.
print(f"{len(added)} {len(removed)} {unchanged}")
