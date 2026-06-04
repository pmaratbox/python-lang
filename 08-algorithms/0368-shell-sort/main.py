def shell_sort(a):
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            tmp = a[i]
            j = i
            while j >= gap and a[j - gap] > tmp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = tmp
        gap //= 2
    return a


print(" ".join(str(x) for x in shell_sort([5, 2, 8, 1, 9, 3])))
