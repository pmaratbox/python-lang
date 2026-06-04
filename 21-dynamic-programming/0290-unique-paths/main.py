def unique_paths(rows, cols):
    dp = [1] * cols
    for _ in range(1, rows):
        for c in range(1, cols):
            dp[c] += dp[c - 1]
    return dp[-1]


def main():
    print(unique_paths(3, 3))


if __name__ == "__main__":
    main()
