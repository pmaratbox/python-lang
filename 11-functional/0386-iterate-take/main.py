from itertools import islice


def iterate(f, x):
    while True:
        yield x
        x = f(x)


def main():
    values = list(islice(iterate(lambda x: x * 3, 1), 4))
    print(" ".join(str(x) for x in values))


if __name__ == "__main__":
    main()
