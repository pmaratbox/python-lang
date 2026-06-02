m = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in m.items()}
print(" ".join(f"{k}:{inverted[k]}" for k in sorted(inverted)))
