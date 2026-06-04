class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, count):
        # Sum of the first `count` elements.
        total = 0
        i = count
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total


data = [1, 2, 3, 4, 5]
bit = Fenwick(len(data))
for i, val in enumerate(data):
    bit.update(i, val)

print(bit.prefix_sum(4))
