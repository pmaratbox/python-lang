def reverse_byte(x):
    result = 0
    for _ in range(8):
        result = (result << 1) | (x & 1)
        x >>= 1
    return result


def main():
    print(reverse_byte(1))


if __name__ == "__main__":
    main()
