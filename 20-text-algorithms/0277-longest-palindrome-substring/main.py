def longest_palindrome(s):
    best = ""
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            cand = s[lo + 1:hi]
            if len(cand) > len(best):
                best = cand
    return best


print(longest_palindrome("babad"))
