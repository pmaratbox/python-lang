scores = {"a": 3, "b": 1, "c": 2}
items = sorted(scores.items(), key=lambda kv: kv[1])
print(" ".join(f"{k}:{v}" for k, v in items))
