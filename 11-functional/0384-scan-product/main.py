from itertools import accumulate
from operator import mul


def main():
    products = list(accumulate([1, 2, 3, 4], mul))
    print(" ".join(str(x) for x in products))


if __name__ == "__main__":
    main()
