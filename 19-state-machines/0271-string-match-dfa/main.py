def first_match(text, pattern):
    state = 0
    for i, ch in enumerate(text):
        if ch == pattern[state]:
            state += 1
            if state == len(pattern):
                return i - len(pattern) + 1
        else:
            state = 1 if ch == pattern[0] else 0
    return -1


def main():
    print(first_match("aab", "ab"))


if __name__ == "__main__":
    main()
