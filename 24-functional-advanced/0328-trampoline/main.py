def trampoline(thunk):
    while callable(thunk):
        thunk = thunk()
    return thunk


def sum_to(n, acc=0):
    if n == 0:
        return acc
    return lambda: sum_to(n - 1, acc + n)


def main():
    print(trampoline(sum_to(100)))


if __name__ == "__main__":
    main()
