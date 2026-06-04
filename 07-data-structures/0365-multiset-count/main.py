from collections import Counter


class MultisetCount:
    def __init__(self):
        self.counts = Counter()

    def add(self, value):
        self.counts[value] += 1

    def remove(self, value):
        if self.counts[value] > 0:
            self.counts[value] -= 1
            if self.counts[value] == 0:
                del self.counts[value]

    def count(self, value):
        return self.counts[value]


def main():
    bag = MultisetCount()
    bag.add(1)
    bag.add(1)
    bag.add(2)
    first = bag.count(1)
    bag.remove(1)
    second = bag.count(1)
    print(first, second)


if __name__ == "__main__":
    main()
