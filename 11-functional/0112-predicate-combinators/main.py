def p_and(p, q):
    return lambda x: p(x) and q(x)


def is_even(x):
    return x % 2 == 0


def is_positive(x):
    return x > 0


pred = p_and(is_even, is_positive)
print("yes" if pred(4) else "no", "yes" if pred(-4) else "no")
