def check(actual, expected):
    if actual != expected:
        raise AssertionError("expected {!r}, got {!r}".format(expected, actual))


def main():
    check(1 + 1, 2)
    check(2 * 3, 6)
    check("ab" + "c", "abc")
    print("all passed")


if __name__ == "__main__":
    main()
