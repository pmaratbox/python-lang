def main():
    mask = 5
    subs = []
    sub = mask
    while True:
        subs.append(sub)
        if sub == 0:
            break
        sub = (sub - 1) & mask
    print(*subs)


if __name__ == "__main__":
    main()
