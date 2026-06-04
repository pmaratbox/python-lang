nums = [1, 2, 3, 4]
pairs = [f"{a},{b}" for a, b in zip(nums, nums[1:])]
print(" ".join(pairs))
