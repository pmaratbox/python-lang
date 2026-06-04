def binomial(n: int, k: int) -> int:
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


print(binomial(5, 2))
