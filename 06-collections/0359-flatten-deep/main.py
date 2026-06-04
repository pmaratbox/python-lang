def flatten(item):
    if isinstance(item, list):
        for sub in item:
            yield from flatten(sub)
    else:
        yield item


data = [1, [2, [3, 4]], 5]
print(" ".join(str(x) for x in flatten(data)))
