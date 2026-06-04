import threading
import queue


def main():
    ch = queue.Queue()

    def producer():
        for v in (1, 2, 3):
            ch.put(v)
        ch.put(None)

    t = threading.Thread(target=producer)
    t.start()

    received = []
    while True:
        v = ch.get()
        if v is None:
            break
        received.append(v)
    t.join()
    print(" ".join(str(v) for v in received))


if __name__ == "__main__":
    main()
