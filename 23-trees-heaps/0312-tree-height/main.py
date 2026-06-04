class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)

print(height(root))
