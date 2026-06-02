nums = [1, 2, 3, 4, 5]
k = 2
rotated = nums[k:] + nums[:k]
print(" ".join(str(x) for x in rotated))
