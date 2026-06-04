import threading
import queue


def main():
    ch = queue.Queue(maxsize=2)

    def producer():
        for v in range(1, 6):
            ch.put(v)
        ch.put(None)

    t = threading.Thread(target=producer)
    t.start()

    total = 0
    while True:
        v = ch.get()
        if v is None:
            break
        total += v
    t.join()
    print(total)


if __name__ == "__main__":
    main()
