from itertools import groupby


def main():
    data = [1, 1, 2, 3, 3, 3]
    runs = [list(g) for _, g in groupby(data)]
    print("|".join(" ".join(str(x) for x in run) for run in runs))


if __name__ == "__main__":
    main()
