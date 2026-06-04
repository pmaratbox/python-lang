from functools import reduce


def compose(f, g):
    return lambda x: f(g(x))


def square(x):
    return x * x


sum_of_squares = compose(sum, lambda xs: map(square, xs))


def main():
    print(sum_of_squares([1, 2, 3]))


if __name__ == "__main__":
    main()
