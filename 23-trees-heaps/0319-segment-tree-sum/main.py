class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i, val in enumerate(data):
            self.tree[self.n + i] = val
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, lo, hi):
        # Sum of indices [lo, hi] inclusive.
        lo += self.n
        hi += self.n + 1
        total = 0
        while lo < hi:
            if lo & 1:
                total += self.tree[lo]
                lo += 1
            if hi & 1:
                hi -= 1
                total += self.tree[hi]
            lo //= 2
            hi //= 2
        return total


tree = SegmentTree([1, 2, 3, 4, 5])
print(tree.query(1, 3))
