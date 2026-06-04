def power_set(items):
    n = len(items)
    for mask in range(1 << n):
        subset = [items[i] for i in range(n) if mask & (1 << i)]
        yield subset


if __name__ == "__main__":
    for subset in power_set([1, 2, 3]):
        if subset:
            print(" ".join(str(x) for x in subset))
        else:
            print("{}")
