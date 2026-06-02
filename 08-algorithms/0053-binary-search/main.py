nums = [1, 3, 5, 7, 9]
target = 7

lo, hi = 0, len(nums) - 1
index = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        index = mid
        break
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

print(f"found {target} at index {index}")
