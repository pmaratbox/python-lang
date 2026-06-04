from functools import reduce


def pipe(*fns):
    return lambda x: reduce(lambda acc, f: f(acc), fns, x)


inc = lambda x: x + 1
double = lambda x: x * 2
neg = lambda x: -x

print(pipe(inc, double, neg)(3))
