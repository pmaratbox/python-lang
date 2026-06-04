def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


print(" ".join(str(x) for x in selection_sort([5, 1, 4, 2])))
