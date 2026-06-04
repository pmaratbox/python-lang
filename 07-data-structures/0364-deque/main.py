from collections import deque


def main():
    items = deque()
    items.append(1)
    items.append(2)
    items.appendleft(0)
    print(" ".join(str(x) for x in items))


if __name__ == "__main__":
    main()
