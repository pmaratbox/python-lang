def zip_with(f, xs, ys):
    return [f(x, y) for x, y in zip(xs, ys)]


result = zip_with(lambda a, b: a + b, [1, 2, 3], [4, 5, 6])
print(" ".join(str(n) for n in result))
