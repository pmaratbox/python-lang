import toolz

result = toolz.mapcat(lambda x: [x, x * 10], [1, 2, 3])
print(",".join(map(str, result)))
