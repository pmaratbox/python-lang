from collections import Counter

nums = [1, 1, 2, 3, 3, 3]
counts = Counter(nums)
# ties keep first-seen order: Counter preserves insertion order, and
# sorted is stable, so sorting by count descending keeps first-seen ties.
ordered = sorted(counts, key=lambda v: counts[v], reverse=True)
result = []
for v in ordered:
    result.extend([v] * counts[v])
print(" ".join(str(x) for x in result))
