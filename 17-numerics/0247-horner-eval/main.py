coeffs = [2, 3, 1]  # 2x^2 + 3x + 1
x = 2
result = 0
for c in coeffs:
    result = result * x + c
print(result)
