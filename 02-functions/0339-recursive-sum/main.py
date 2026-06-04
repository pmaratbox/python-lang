def rsum(xs):
    if not xs:
        return 0
    return xs[0] + rsum(xs[1:])


print(rsum([1, 2, 3, 4]))
