from concurrent.futures import ThreadPoolExecutor


def square(n):
    return n * n


def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(square, range(1, 5)))
    results.sort()
    print(" ".join(str(v) for v in results))


if __name__ == "__main__":
    main()
