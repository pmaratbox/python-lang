rows = [("a", "1"), ("bb", "22")]

width = max(len(first) for first, _ in rows)

for first, second in rows:
    print("{} | {}".format(first.ljust(width), second))
