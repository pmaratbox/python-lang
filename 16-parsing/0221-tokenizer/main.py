def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c.isdigit():
            tokens.append("NUM")
            i += 1
            while i < len(s) and s[i].isdigit():
                i += 1
        elif c == "+":
            tokens.append("PLUS")
            i += 1
        else:
            i += 1
    return tokens


print(" ".join(tokenize("1 + 2")))
