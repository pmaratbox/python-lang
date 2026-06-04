def main():
    codes = [n ^ (n >> 1) for n in range(4)]
    print(*codes)


if __name__ == "__main__":
    main()
