def expand_range(spec):
    start, end = spec.split("-")
    return "".join(chr(code) for code in range(ord(start), ord(end) + 1))


print(expand_range("a-e"))
