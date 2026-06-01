letters = ["a", "b", "c"]
nums = [1, 2, 3]
pairs = [f"{k}={n}" for k, n in zip(letters, nums)]
print(" ".join(pairs))
