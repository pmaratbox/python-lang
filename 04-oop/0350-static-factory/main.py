class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_hex(cls, code):
        code = code.lstrip("#")
        r = int(code[0:2], 16)
        g = int(code[2:4], 16)
        b = int(code[4:6], 16)
        return cls(r, g, b)


def main():
    color = Color.from_hex("#ff0000")
    print(color.r, color.g, color.b)


if __name__ == "__main__":
    main()
