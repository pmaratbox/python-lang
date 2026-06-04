class RangeIterator:
    def __init__(self, start, end):
        self._current = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._end:
            raise StopIteration
        value = self._current
        self._current += 1
        return value


def main():
    print(" ".join(str(v) for v in RangeIterator(1, 3)))


if __name__ == "__main__":
    main()
