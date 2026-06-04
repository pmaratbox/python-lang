def main():
    floor = 0
    stops = [floor]
    for target in (2, 0):
        step = 1 if target > floor else -1
        while floor != target:
            floor += step
            stops.append(floor)
    print(" ".join(str(f) for f in stops))


if __name__ == "__main__":
    main()
