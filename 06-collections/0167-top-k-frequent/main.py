from collections import Counter

data = ["a", "b", "a", "c", "b", "a"]
counts = Counter(data)
top = [item for item, _ in counts.most_common(2)]
print(" ".join(top))
