def rot13(s):
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - ord("A") + 13) % 26 + ord("A")))
        else:
            out.append(ch)
    return "".join(out)


encoded = rot13("hello")
print(encoded, rot13(encoded))
