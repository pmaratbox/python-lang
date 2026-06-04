a = [1, 2, 3]
b = ["a", "b"]
n = max(len(a), len(b))
parts = []
for i in range(n):
    x = a[i] if i < len(a) else "-"
    y = b[i] if i < len(b) else "-"
    parts.append(f"{x}{y}")
print(" ".join(parts))
