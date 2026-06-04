def min_max(xs):
    lo = hi = xs[0]
    for x in xs[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi


lo, hi = min_max([4, 1, 7])
print(lo, hi)
