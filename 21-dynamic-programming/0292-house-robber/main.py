def rob(houses):
    prev, curr = 0, 0
    for x in houses:
        prev, curr = curr, max(curr, prev + x)
    return curr


def main():
    print(rob([2, 7, 9, 3, 1]))


if __name__ == "__main__":
    main()
