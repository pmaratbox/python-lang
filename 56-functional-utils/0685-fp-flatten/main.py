import toolz

nested = [[1, 2], [3, 4], [5, 6]]
flattened = toolz.concat(nested)
print(",".join(map(str, flattened)))
