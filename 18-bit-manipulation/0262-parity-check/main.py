def parity(n):
    return bin(n).count("1") & 1


def main():
    print(parity(7), parity(5))


if __name__ == "__main__":
    main()
