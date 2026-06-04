def main():
    x = 1
    outputs = []
    for _ in range(3):
        x = (5 * x + 3) % 16
        outputs.append(str(x))
    print(" ".join(outputs))


if __name__ == "__main__":
    main()
