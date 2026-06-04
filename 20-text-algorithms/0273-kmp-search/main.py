def prefix_function(p):
    pi = [0] * len(p)
    k = 0
    for i in range(1, len(p)):
        while k > 0 and p[i] != p[k]:
            k = pi[k - 1]
        if p[i] == p[k]:
            k += 1
        pi[i] = k
    return pi


def kmp_search(text, pattern):
    pi = prefix_function(pattern)
    res = []
    k = 0
    for i, ch in enumerate(text):
        while k > 0 and ch != pattern[k]:
            k = pi[k - 1]
        if ch == pattern[k]:
            k += 1
        if k == len(pattern):
            res.append(i - k + 1)
            k = pi[k - 1]
    return res


print(" ".join(str(i) for i in kmp_search("ababab", "ab")))
