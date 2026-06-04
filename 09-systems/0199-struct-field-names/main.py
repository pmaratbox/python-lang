from dataclasses import dataclass, fields


@dataclass
class Point:
    x: int
    y: int


def main():
    print(" ".join(f.name for f in fields(Point)))


if __name__ == "__main__":
    main()
