def bubble_sort(values):
    a = list(values)
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == "__main__":
    result = bubble_sort([5, 1, 4, 2, 8])
    print(" ".join(str(x) for x in result))
