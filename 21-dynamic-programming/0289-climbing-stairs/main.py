def climb(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    print(climb(5))


if __name__ == "__main__":
    main()
