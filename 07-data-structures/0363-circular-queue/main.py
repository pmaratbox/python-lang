class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise IndexError("queue is full")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("queue is empty")
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def items(self):
        return [self.buffer[(self.head + i) % self.capacity] for i in range(self.size)]


def main():
    queue = CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(4)
    print(" ".join(str(x) for x in queue.items()))


if __name__ == "__main__":
    main()
