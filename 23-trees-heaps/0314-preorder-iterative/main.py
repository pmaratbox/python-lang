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


root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)

out = []
stack = [root]
while stack:
    node = stack.pop()
    out.append(node.val)
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)

print(" ".join(str(x) for x in out))
