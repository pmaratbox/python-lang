def insertion_sort(values):
    a = list(values)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    result = insertion_sort([5, 1, 4, 2, 8])
    print(" ".join(str(x) for x in result))
