from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


if __name__ == "__main__":
    print(lcm(4, 6))
