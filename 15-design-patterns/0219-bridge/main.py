class Red:
    def name(self):
        return "red"


class Circle:
    def __init__(self, color):
        self._color = color

    def describe(self):
        return "{} circle".format(self._color.name())


def main():
    print(Circle(Red()).describe())


if __name__ == "__main__":
    main()
