def flat_map(f, items):
    return [y for x in items for y in f(x)]


def main():
    result = flat_map(lambda x: [x, x * 10], [1, 2, 3])
    print(" ".join(str(n) for n in result))


if __name__ == "__main__":
    main()
