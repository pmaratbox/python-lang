class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head = Node(1, Node(2, Node(3)))

parts = []
node = head
while node is not None:
    parts.append(str(node.value))
    node = node.next
print(" -> ".join(parts))
