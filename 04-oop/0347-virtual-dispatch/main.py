class Shape:
    def describe(self):
        raise NotImplementedError


class Circle(Shape):
    def describe(self):
        return "circle"


class Square(Shape):
    def describe(self):
        return "square"


class Triangle(Shape):
    def describe(self):
        return "triangle"


def main():
    shapes = [Circle(), Square(), Triangle()]
    print(" ".join(shape.describe() for shape in shapes))


if __name__ == "__main__":
    main()
