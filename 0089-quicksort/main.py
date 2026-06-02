def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[0]
    rest = items[1:]
    less = [x for x in rest if x < pivot]
    greater = [x for x in rest if x >= pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


data = [3, 1, 4, 1, 5, 2]
print(" ".join(str(x) for x in quicksort(data)))
