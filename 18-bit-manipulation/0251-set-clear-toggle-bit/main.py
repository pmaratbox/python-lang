def main():
    pos = 1
    set_ = 0 | (1 << pos)
    cleared = 2 & ~(1 << pos)
    toggled = 0 ^ (1 << pos)
    print(set_, cleared, toggled)


if __name__ == "__main__":
    main()
