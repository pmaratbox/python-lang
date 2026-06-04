class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1


def main():
    InstanceCounter()
    InstanceCounter()
    InstanceCounter()
    print(InstanceCounter.count)


if __name__ == "__main__":
    main()
