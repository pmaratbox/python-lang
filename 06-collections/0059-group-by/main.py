from collections import defaultdict

words = ["one", "two", "three"]
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)

parts = [f"{k}:[{','.join(groups[k])}]" for k in sorted(groups)]
print(" ".join(parts))
