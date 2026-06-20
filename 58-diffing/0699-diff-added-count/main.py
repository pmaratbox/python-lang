import difflib

# Diff two fixed line-lists with the stdlib difflib library.
a = ["apple", "banana", "cherry"]
b = ["apple", "blueberry", "cherry", "date"]

# SequenceMatcher.get_opcodes() yields LCS-determined edit operations.
# "insert"/"replace" contribute target lines as ADDED; a "replace" maps a
# CHANGE delta to removed(source)+added(target).
sm = difflib.SequenceMatcher(None, a, b)
added = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("insert", "replace"):
        added += b[j1:j2]

# Print the count of ADDED lines.
print(len(added))
