def main():
    r, g, b = 1, 2, 3
    packed = (r << 16) | (g << 8) | b
    ur = (packed >> 16) & 0xFF
    ug = (packed >> 8) & 0xFF
    ub = packed & 0xFF
    print(ur, ug, ub)


if __name__ == "__main__":
    main()
