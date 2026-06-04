def multiply(a: str, b: str) -> str:
    res = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            p = int(a[i]) * int(b[j])
            s = p + res[i + j + 1]
            res[i + j + 1] = s % 10
            res[i + j] += s // 10
    digits = "".join(str(d) for d in res).lstrip("0")
    return digits or "0"


print(multiply("123", "456"))
