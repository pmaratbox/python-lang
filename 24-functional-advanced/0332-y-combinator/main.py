def Y(f):
    return (lambda x: f(lambda *args: x(x)(*args)))(
        lambda x: f(lambda *args: x(x)(*args))
    )


def fact_gen(rec):
    return lambda n: 1 if n == 0 else n * rec(n - 1)


def main():
    factorial = Y(fact_gen)
    print(factorial(5))


if __name__ == "__main__":
    main()
