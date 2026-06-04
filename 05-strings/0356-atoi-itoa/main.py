def atoi(s):
    i = 0
    sign = 1
    if s and s[0] in "+-":
        if s[0] == "-":
            sign = -1
        i = 1
    value = 0
    while i < len(s):
        value = value * 10 + (ord(s[i]) - ord("0"))
        i += 1
    return sign * value


def itoa(n):
    if n == 0:
        return "0"
    neg = n < 0
    n = abs(n)
    digits = []
    while n > 0:
        digits.append(chr(ord("0") + n % 10))
        n //= 10
    if neg:
        digits.append("-")
    return "".join(reversed(digits))


parsed = atoi("-42")
print(parsed, itoa(parsed))
