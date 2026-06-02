class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(root, out):
    if root is None:
        return
    inorder(root.left, out)
    out.append(str(root.value))
    inorder(root.right, out)


root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)

out = []
inorder(root, out)
print(" ".join(out))
