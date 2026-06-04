class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []


best = 0


def height(node):
    global best
    if node is None:
        return 0
    heights = sorted((height(c) for c in node.children), reverse=True)
    top_two = heights[:2] + [0, 0]
    best = max(best, top_two[0] + top_two[1])
    return 1 + (heights[0] if heights else 0)


c = Node("C")
d = Node("D")
a = Node("A", [c, d])
b = Node("B")
root = Node("root", [a, b])

height(root)
print(best)
