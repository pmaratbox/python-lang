def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)


for n in (4, 3):
    print("even" if is_even(n) else "odd")
