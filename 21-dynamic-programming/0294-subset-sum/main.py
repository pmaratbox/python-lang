def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            if dp[s - x]:
                dp[s] = True
    return dp[target]


def main():
    print("yes" if subset_sum([3, 34, 4, 12, 5, 2], 9) else "no")


if __name__ == "__main__":
    main()
