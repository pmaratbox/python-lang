from collections import Counter


def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    best = ""
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if not best or right - left + 1 < len(best):
                best = s[left:right + 1]
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return best


print(min_window("ADOBECODEBANC", "ABC"))
