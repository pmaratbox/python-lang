import threading


class OnceInit:
    def __init__(self):
        self.count = 0
        self._done = False
        self._lock = threading.Lock()

    def init(self):
        if self._done:
            return
        with self._lock:
            if not self._done:
                self.count += 1
                self._done = True


def main():
    once = OnceInit()

    def race():
        once.init()

    threads = [threading.Thread(target=race) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("init count: {}".format(once.count))


if __name__ == "__main__":
    main()
