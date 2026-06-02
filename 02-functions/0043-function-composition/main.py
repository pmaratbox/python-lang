def inc(x: int) -> int:
    return x + 1

def twice(x: int) -> int:
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

print(compose(inc, twice)(3))
