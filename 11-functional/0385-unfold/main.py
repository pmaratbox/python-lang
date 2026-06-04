def unfold(seed, nxt, count):
    x = seed
    for _ in range(count):
        yield x
        x = nxt(x)


def main():
    terms = list(unfold(1, lambda x: x * 2, 5))
    print(" ".join(str(x) for x in terms))


if __name__ == "__main__":
    main()
