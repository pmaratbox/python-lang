nums = [1, 2, 3, 4]
size = 2
for i in range(len(nums) - size + 1):
    window = nums[i:i + size]
    print(" ".join(str(x) for x in window))
