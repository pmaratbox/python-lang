from itertools import count, islice


def naturals():
    yield from count(1)


def main():
    first_five = list(islice(naturals(), 5))
    print(" ".join(str(n) for n in first_five))


if __name__ == "__main__":
    main()
