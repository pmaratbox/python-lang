nums = [1, 2, 3, 4, 5, 6, 7]
size = 3
for i in range(0, len(nums), size):
    chunk = nums[i:i + size]
    print(" ".join(str(x) for x in chunk))
