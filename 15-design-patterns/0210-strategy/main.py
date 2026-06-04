def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def apply(strategy, a, b):
    return strategy(a, b)


def main():
    strategies = {"add": add, "mul": mul}
    print(apply(strategies["add"], 3, 4), apply(strategies["mul"], 3, 4))


if __name__ == "__main__":
    main()
