left = {"a": 1, "b": 2}
right = {"b": 3, "c": 4}
merged = {**left, **right}
print(" ".join(f"{k}:{merged[k]}" for k in sorted(merged)))
