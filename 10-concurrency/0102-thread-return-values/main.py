import threading


def square(n, results, idx):
    results[idx] = n * n


def main():
    results = [0, 0]
    t1 = threading.Thread(target=square, args=(3, results, 0))
    t2 = threading.Thread(target=square, args=(4, results, 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(results[0] + results[1])


if __name__ == "__main__":
    main()
