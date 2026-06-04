def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


if __name__ == "__main__":
    print("yes" if is_happy(19) else "no")
