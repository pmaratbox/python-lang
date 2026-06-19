import toolz

print(",".join(map(str, toolz.filter(lambda x: x % 2 == 0, range(1, 7)))))
