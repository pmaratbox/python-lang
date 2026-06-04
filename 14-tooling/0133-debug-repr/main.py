class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)


def main():
    p = Point(1, 2)
    print(repr(p))


if __name__ == "__main__":
    main()
