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


def search(root, val):
    if root is None:
        return False
    if val == root.val:
        return True
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)


root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)

print("yes" if search(root, 4) else "no", "yes" if search(root, 6) else "no")
