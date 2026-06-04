def main():
    price = 25
    total = 0
    for coin in (10, 10, 5):
        total += coin
    if total >= price:
        print("dispensed")


if __name__ == "__main__":
    main()
