def divisible_by_3(bits):
    state = 0
    for ch in bits:
        state = (state * 2 + int(ch)) % 3
    return state == 0


def main():
    results = ["yes" if divisible_by_3(b) else "no" for b in ("110", "100")]
    print(" ".join(results))


if __name__ == "__main__":
    main()
