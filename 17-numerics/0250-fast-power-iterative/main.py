def fast_pow(base: int, exp: int) -> int:
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result


print(fast_pow(2, 10))
