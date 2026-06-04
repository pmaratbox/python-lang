def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(cur + x, x)
        best = max(best, cur)
    return best


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
