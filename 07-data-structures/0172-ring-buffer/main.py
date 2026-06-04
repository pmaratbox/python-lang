class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.start = 0
        self.size = 0

    def push(self, value):
        end = (self.start + self.size) % self.capacity
        self.data[end] = value
        if self.size < self.capacity:
            self.size += 1
        else:
            self.start = (self.start + 1) % self.capacity

    def items(self):
        return [self.data[(self.start + i) % self.capacity] for i in range(self.size)]


def main():
    buf = Buffer(3)
    for value in (1, 2, 3, 4, 5):
        buf.push(value)
    print(" ".join(str(v) for v in buf.items()))


if __name__ == "__main__":
    main()
