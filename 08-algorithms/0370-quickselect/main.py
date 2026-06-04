def quickselect(a, k):
    pivot = a[len(a) // 2]
    lo = [x for x in a if x < pivot]
    eq = [x for x in a if x == pivot]
    hi = [x for x in a if x > pivot]
    if k < len(lo):
        return quickselect(lo, k)
    if k < len(lo) + len(eq):
        return pivot
    return quickselect(hi, k - len(lo) - len(eq))


print(quickselect([7, 10, 4, 3, 20, 15], 2))
