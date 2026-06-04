def main():
    nxt = {"red": "green", "green": "yellow", "yellow": "red"}
    state = "red"
    states = []
    for _ in range(4):
        state = nxt[state]
        states.append(state)
    print(" ".join(states))


if __name__ == "__main__":
    main()
