import itertools

nums = [1, 2]
letters = ["a", "b"]
pairs = [f"{n}{c}" for n, c in itertools.product(nums, letters)]
print(" ".join(pairs))
