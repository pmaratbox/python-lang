from itertools import count, islice


def naturals():
    yield from count(1)


def main():
    evens = filter(lambda n: n % 2 == 0, naturals())
    first_three = list(islice(evens, 3))
    print(" ".join(str(n) for n in first_three))


if __name__ == "__main__":
    main()
