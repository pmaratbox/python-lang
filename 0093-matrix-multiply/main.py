a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
n = 2
result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += a[i][k] * b[k][j]

for row in result:
    print(" ".join(str(x) for x in row))
