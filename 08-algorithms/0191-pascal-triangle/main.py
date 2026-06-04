def pascal_triangle(rows):
    triangle = []
    row = [1]
    for _ in range(rows):
        triangle.append(row)
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return triangle


if __name__ == "__main__":
    for row in pascal_triangle(4):
        print(" ".join(str(x) for x in row))
