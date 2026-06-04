from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def main():
    print(" ".join(c.name for c in Color))


if __name__ == "__main__":
    main()
