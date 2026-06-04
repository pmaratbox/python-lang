def main():
    nxt = {"A": "B", "B": "C", "C": "A"}
    state = "A"
    visited = []
    for _ in range(3):
        state = nxt[state]
        visited.append(state)
    print(" ".join(visited))


if __name__ == "__main__":
    main()
