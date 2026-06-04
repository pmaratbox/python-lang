seen = set()
result = []
for ch in "aabbcc":
    if ch not in seen:
        seen.add(ch)
        result.append(ch)
print("".join(result))
