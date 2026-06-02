cache = {}


def fib(n):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


print(fib(10))
