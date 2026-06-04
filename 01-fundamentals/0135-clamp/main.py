def clamp(x, lo, hi):
    return max(lo, min(x, hi))


print(clamp(15, 0, 10), clamp(-3, 0, 10))
