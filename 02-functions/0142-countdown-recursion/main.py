def countdown(n):
    if n < 1:
        return []
    return [n] + countdown(n - 1)


print(" ".join(str(x) for x in countdown(5)))
