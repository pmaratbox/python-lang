class Leaf:
    def __init__(self, value):
        self.value = value

    def size(self):
        return self.value


class Composite:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def size(self):
        return sum(child.size() for child in self.children)


def main():
    tree = Composite()
    for v in (1, 2, 3):
        tree.add(Leaf(v))
    print(tree.size())


if __name__ == "__main__":
    main()
