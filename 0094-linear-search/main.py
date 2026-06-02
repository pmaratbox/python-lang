nums = [4, 2, 7, 1, 9]
target = 7
index = -1
for i, n in enumerate(nums):
    if n == target:
        index = i
        break
print(f"found {target} at index {index}")
