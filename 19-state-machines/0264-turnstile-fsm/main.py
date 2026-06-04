def main():
    table = {
        ("locked", "coin"): "unlocked",
        ("unlocked", "push"): "locked",
        ("locked", "push"): "locked",
        ("unlocked", "coin"): "unlocked",
    }
    state = "locked"
    results = []
    for event in ("coin", "push", "push"):
        state = table[(state, event)]
        results.append(state)
    print(" ".join(results))


if __name__ == "__main__":
    main()
