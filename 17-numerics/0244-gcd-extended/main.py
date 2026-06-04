def ext_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


g, x, y = ext_gcd(30, 12)
print("{} {} {}".format(g, x, y))
