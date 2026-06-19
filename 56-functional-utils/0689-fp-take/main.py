import toolz

print(",".join(map(str, toolz.take(3, range(1, 11)))))  # 1,2,3
