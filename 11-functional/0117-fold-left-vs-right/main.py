from functools import reduce


def foldl(f, acc, xs):
    return reduce(f, xs, acc)


def foldr(f, acc, xs):
    result = acc
    for x in reversed(xs):
        result = f(x, result)
    return result


sub = lambda a, b: a - b
left = foldl(sub, 0, [1, 2, 3])
right = foldr(sub, 0, [1, 2, 3])
print(left, right)
