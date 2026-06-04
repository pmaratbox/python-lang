def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def main():
    print("yes" if is_power_of_two(16) else "no",
          "yes" if is_power_of_two(18) else "no")


if __name__ == "__main__":
    main()
