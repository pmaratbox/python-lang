def rol8(x, n):
    return ((x << n) | (x >> (8 - n))) & 0xFF


def main():
    print(rol8(1, 1), rol8(128, 1))


if __name__ == "__main__":
    main()
