# 0064 — Matrix Transpose

Transpose the 2x3 matrix `[[1, 2, 3], [4, 5, 6]]` (swap rows and columns) and print the resulting 3x2 matrix, one row per line: `1 4`, `2 5`, `3 6`. `zip(*matrix)` unpacks the rows as arguments and zips them, pairing element `j` of every row — which is exactly column `j` of the transpose.

## Run

    python3 main.py
