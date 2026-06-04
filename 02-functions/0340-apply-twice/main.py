def apply_twice(f, x):
    return f(f(x))


def inc(n):
    return n + 1


print(apply_twice(inc, 3))
