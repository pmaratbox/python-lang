def main():
    a, b = 3, 5
    a ^= b
    b ^= a
    a ^= b
    print(a, b)


if __name__ == "__main__":
    main()
