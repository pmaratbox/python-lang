import threading
import itertools


def main():
    # CPython has no lock-free atomic int, but itertools.count().__next__ is
    # itself atomic (implemented in C, runs under the GIL as one step), so
    # concurrent next() calls never lose an increment — a lock-free counter.
    counter = itertools.count()

    def work():
        for _ in range(100):
            next(counter)

    threads = [threading.Thread(target=work) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(next(counter))


if __name__ == "__main__":
    main()
