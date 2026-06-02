text = "abc"
shift = 1
result = "".join(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")) for ch in text)
print(result)
