def check(arg):
    if arg <= 0:
        raise ValueError("must be positive")
    return "ok"


def main():
    for arg in (5, -1):
        try:
            print(check(arg))
        except ValueError as e:
            print("error: {}".format(e))


if __name__ == "__main__":
    main()
