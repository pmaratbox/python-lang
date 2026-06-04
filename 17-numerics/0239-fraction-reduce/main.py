from math import gcd

num, den = 6, 8
g = gcd(num, den)
print("{}/{}".format(num // g, den // g))
