def rule90(row):
    n = len(row)
    out = []
    for i in range(n):
        left = row[i - 1] if i - 1 >= 0 else 0
        right = row[i + 1] if i + 1 < n else 0
        out.append(left ^ right)
    return out


def main():
    row = [int(c) for c in "00100"]
    row = rule90(row)
    print("".join(str(b) for b in row))


if __name__ == "__main__":
    main()
