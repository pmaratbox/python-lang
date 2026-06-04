class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node


def main():
    lst = LinkedList()
    for value in (1, 2, 3):
        lst.append(value)

    forward = []
    node = lst.head
    while node is not None:
        forward.append(str(node.value))
        node = node.next
    print(" ".join(forward))

    backward = []
    node = lst.tail
    while node is not None:
        backward.append(str(node.value))
        node = node.prev
    print(" ".join(backward))


if __name__ == "__main__":
    main()
