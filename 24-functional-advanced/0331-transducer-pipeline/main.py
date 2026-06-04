def mapping(f):
    return lambda step: lambda acc, x: step(acc, f(x))


def filtering(pred):
    return lambda step: lambda acc, x: step(acc, x) if pred(x) else acc


def compose(*xforms):
    def composed(step):
        for xf in reversed(xforms):
            step = xf(step)
        return step
    return composed


def main():
    xform = compose(mapping(lambda x: x + 1), filtering(lambda x: x % 2 == 0))

    def append(acc, x):
        acc.append(x)
        return acc

    reducer = xform(append)
    result = []
    for item in [1, 2, 3, 4]:
        result = reducer(result, item)
    print(" ".join(str(n) for n in result))


if __name__ == "__main__":
    main()
