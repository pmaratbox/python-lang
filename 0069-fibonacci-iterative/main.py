a, b = 0, 1
nums = []
for _ in range(7):
    nums.append(str(a))
    a, b = b, a + b
print(" ".join(nums))
