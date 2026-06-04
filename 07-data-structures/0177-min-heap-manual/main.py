class HeapManual:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def pop(self):
        last = len(self.data) - 1
        self.data[0], self.data[last] = self.data[last], self.data[0]
        result = self.data.pop()
        i = 0
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest
        return result


def main():
    heap = HeapManual()
    for value in (3, 1, 2):
        heap.push(value)
    out = [heap.pop() for _ in range(3)]
    print(" ".join(str(v) for v in out))


if __name__ == "__main__":
    main()
