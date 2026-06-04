def rabin_karp(text, pattern):
    base, mod = 256, 1_000_000_007
    m, n = len(pattern), len(text)
    if m > n:
        return []
    high = pow(base, m - 1, mod)
    ph = th = 0
    for i in range(m):
        ph = (ph * base + ord(pattern[i])) % mod
        th = (th * base + ord(text[i])) % mod
    res = []
    for i in range(n - m + 1):
        if ph == th and text[i:i + m] == pattern:
            res.append(i)
        if i < n - m:
            th = ((th - ord(text[i]) * high) * base + ord(text[i + m])) % mod
    return res


print(" ".join(str(i) for i in rabin_karp("xabxab", "ab")))
