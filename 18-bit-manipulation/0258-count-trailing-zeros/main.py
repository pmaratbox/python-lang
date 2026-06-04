def trailing_zeros(x):
    count = 0
    while (x & 1) == 0:
        count += 1
        x >>= 1
    return count


def main():
    print(trailing_zeros(8))


if __name__ == "__main__":
    main()
