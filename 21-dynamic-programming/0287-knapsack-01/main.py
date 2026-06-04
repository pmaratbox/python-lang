def knapsack(items, capacity):
    dp = [0] * (capacity + 1)
    for w, v in items:
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


def main():
    print(knapsack([(2, 3), (3, 4), (4, 5)], 5))


if __name__ == "__main__":
    main()
