def add(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    out = []
    while i >= 0 or j >= 0 or carry:
        d = carry
        if i >= 0:
            d += int(a[i])
            i -= 1
        if j >= 0:
            d += int(b[j])
            j -= 1
        out.append(str(d % 10))
        carry = d // 10
    return "".join(reversed(out))


print(add("999999999999", "1"))
