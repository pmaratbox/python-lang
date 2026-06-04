class Glyph:
    def __init__(self, char):
        self.char = char


class GlyphFactory:
    def __init__(self):
        self._cache = {}

    def get(self, char):
        if char not in self._cache:
            self._cache[char] = Glyph(char)
        return self._cache[char]

    def count(self):
        return len(self._cache)


def main():
    factory = GlyphFactory()
    for char in ("a", "b", "a"):
        factory.get(char)
    print(factory.count())


if __name__ == "__main__":
    main()
