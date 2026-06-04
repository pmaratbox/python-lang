class Leaf:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_leaf(self)


class Node:
    def __init__(self, children):
        self.children = children

    def accept(self, visitor):
        return visitor.visit_node(self)


class SumVisitor:
    def visit_leaf(self, leaf):
        return leaf.value

    def visit_node(self, node):
        return sum(child.accept(self) for child in node.children)


def main():
    tree = Node([Leaf(1), Leaf(2), Leaf(3)])
    print(tree.accept(SumVisitor()))


if __name__ == "__main__":
    main()
