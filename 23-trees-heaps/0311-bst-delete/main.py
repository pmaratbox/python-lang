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


def delete(root, val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ = root.right
        while succ.left is not None:
            succ = succ.left
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root


def inorder(root, out):
    if root is None:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)


root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)

root = delete(root, 3)
out = []
inorder(root, out)
print(" ".join(str(x) for x in out))
