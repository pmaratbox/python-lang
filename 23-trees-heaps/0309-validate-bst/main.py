class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_bst(node, low=float("-inf"), high=float("inf")):
    if node is None:
        return True
    if not (low < node.val < high):
        return False
    return is_bst(node.left, low, node.val) and is_bst(node.right, node.val, high)


good = Node(5, Node(3, Node(1), Node(4)), Node(8))
bad = Node(5, Node(3, Node(1), Node(9)), Node(8))

print("yes" if is_bst(good) else "no", "yes" if is_bst(bad) else "no")
