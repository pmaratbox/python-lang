text = "aaabbc"
result = []
i = 0
while i < len(text):
    ch = text[i]
    count = 0
    while i < len(text) and text[i] == ch:
        count += 1
        i += 1
    result.append(f"{ch}{count}")
print("".join(result))
