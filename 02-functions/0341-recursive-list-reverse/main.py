def rev(xs):
    if not xs:
        return []
    return rev(xs[1:]) + [xs[0]]


print(" ".join(str(x) for x in rev([1, 2, 3])))
