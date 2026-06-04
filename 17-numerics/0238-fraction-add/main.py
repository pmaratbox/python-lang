from math import gcd

a_num, a_den = 1, 2
b_num, b_den = 1, 3

num = a_num * b_den + b_num * a_den
den = a_den * b_den
g = gcd(num, den)
print("{}/{}".format(num // g, den // g))
