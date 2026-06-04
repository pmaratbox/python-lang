from collections import Counter

counts = Counter("hello")
print(counts.most_common(1)[0][0])
