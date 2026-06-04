def factorial_cps(n, cont):
    if n == 0:
        return cont(1)
    return factorial_cps(n - 1, lambda r: cont(n * r))


def main():
    print(factorial_cps(5, lambda x: x))


if __name__ == "__main__":
    main()
