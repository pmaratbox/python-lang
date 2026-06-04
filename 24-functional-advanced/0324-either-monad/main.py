class Either:
    def __init__(self, value, is_right):
        self.value = value
        self.is_right = is_right

    def bind(self, f):
        if self.is_right:
            return f(self.value)
        return self


def Right(value):
    return Either(value, True)


def Left(tag):
    return Either(tag, False)


def safe_div(a, b):
    if b == 0:
        return Left("err")
    return Right(a // b)


def main():
    ok = Right(8).bind(lambda x: safe_div(x, 2)).bind(lambda x: safe_div(x, 2))
    bad = Right(8).bind(lambda x: safe_div(x, 0)).bind(lambda x: safe_div(x, 2))

    left = str(ok.value) if ok.is_right else ok.value
    right = str(bad.value) if bad.is_right else bad.value
    print(left + " " + right)


if __name__ == "__main__":
    main()
