def sift_down(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def heap_sort(arr):
    n = len(arr)
    for start in range(n // 2 - 1, -1, -1):
        sift_down(arr, start, n - 1)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)


data = [5, 3, 8, 1, 4]
heap_sort(data)
print(" ".join(str(x) for x in data))
