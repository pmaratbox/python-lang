from collections import deque


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
queue = deque([root])
while queue:
    node = queue.popleft()
    out.append(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

print(" ".join(str(x) for x in out))
