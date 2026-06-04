import threading


def worker():
    pass


def main():
    threads = [threading.Thread(target=worker) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("done: {}".format(len(threads)))


if __name__ == "__main__":
    main()
