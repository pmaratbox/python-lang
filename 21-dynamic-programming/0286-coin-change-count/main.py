def count_ways(coins, amount):
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


def main():
    print(count_ways([1, 2, 5], 5))


if __name__ == "__main__":
    main()
