class Lens:
    def __init__(self, getter, setter):
        self.get = getter
        self.set = setter


def key_lens(k):
    def setter(d, v):
        copy = dict(d)
        copy[k] = v
        return copy
    return Lens(lambda d: d[k], setter)


def compose(outer, inner):
    def setter(d, v):
        return outer.set(d, inner.set(outer.get(d), v))
    return Lens(lambda d: inner.get(outer.get(d)), setter)


def main():
    data = {"a": {"b": 1}}
    ab = compose(key_lens("a"), key_lens("b"))
    got = ab.get(data)
    updated = ab.set(data, 2)
    print(str(got) + " " + str(ab.get(updated)))


if __name__ == "__main__":
    main()
