import itertools

def squares():
    n = 1
    while True:
        yield n * n
        n += 1

first3 = list(itertools.islice(squares(), 3))
print(*first3)
