from functools import reduce


def fold(identity, combine, items):
    return reduce(combine, items, identity)


def main():
    s = fold("", lambda a, b: a + b, ["a", "b", "c"])
    n = fold(0, lambda a, b: a + b, [1, 2, 3])
    print(s + " " + str(n))


if __name__ == "__main__":
    main()
