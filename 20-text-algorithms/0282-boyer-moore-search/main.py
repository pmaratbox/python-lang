def boyer_moore(text, pattern):
    last = {c: i for i, c in enumerate(pattern)}
    m = len(pattern)
    n = len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        shift = j - last.get(text[s + j], -1)
        s += max(1, shift)
    return -1


print(boyer_moore("zzabc", "abc"))
