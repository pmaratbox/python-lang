def counting_sort(a):
    counts = [0] * (max(a) + 1)
    for x in a:
        counts[x] += 1
    out = []
    for value, c in enumerate(counts):
        out.extend([value] * c)
    return out


print(" ".join(str(x) for x in counting_sort([3, 1, 2, 3, 1])))
