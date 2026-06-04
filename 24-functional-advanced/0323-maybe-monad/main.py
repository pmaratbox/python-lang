class Maybe:
    def __init__(self, value, present):
        self.value = value
        self.present = present

    def bind(self, f):
        if self.present:
            return f(self.value)
        return self


def Some(value):
    return Maybe(value, True)


NONE = Maybe(None, False)


def main():
    present = Some(2).bind(lambda x: Some(x + 3)).bind(lambda x: Some(x * 2))
    absent = NONE.bind(lambda x: Some(x + 3)).bind(lambda x: Some(x * 2))

    left = str(present.value) if present.present else "none"
    right = str(absent.value) if absent.present else "none"
    print(left + " " + right)


if __name__ == "__main__":
    main()
