from itertools import accumulate

nums = [1, 2, 3, 4]
sums = list(accumulate(nums))
print(" ".join(str(x) for x in sums))
