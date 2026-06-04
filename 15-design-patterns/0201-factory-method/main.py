class Circle:
    kind = "circle"


class Square:
    kind = "square"


def make_shape(name):
    factory = {"circle": Circle, "square": Square}
    return factory[name]()


def main():
    shapes = [make_shape("circle"), make_shape("square")]
    print(" ".join(s.kind for s in shapes))


if __name__ == "__main__":
    main()
