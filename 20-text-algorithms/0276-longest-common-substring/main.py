def longest_common_substring(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    best, end = 0, 0
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            if ca == cb:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best, end = dp[i][j], i
    return a[end - best:end]


print(longest_common_substring("abcde", "xbcdy"))
