import threading


class SharedCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1


def main():
    counter = SharedCounter()

    def work():
        for _ in range(100):
            counter.increment()

    threads = [threading.Thread(target=work) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter.value)


if __name__ == "__main__":
    main()
