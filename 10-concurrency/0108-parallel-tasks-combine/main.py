from concurrent.futures import ThreadPoolExecutor


def task(value):
    return value


def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        f1 = pool.submit(task, 10)
        f2 = pool.submit(task, 20)
        total = f1.result() + f2.result()
    print(total)


if __name__ == "__main__":
    main()
