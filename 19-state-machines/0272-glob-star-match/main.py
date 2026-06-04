def glob_match(pattern, text):
    if not pattern:
        return not text
    if pattern[0] == "*":
        return glob_match(pattern[1:], text) or (
            bool(text) and glob_match(pattern, text[1:])
        )
    return bool(text) and pattern[0] == text[0] and glob_match(pattern[1:], text[1:])


def main():
    results = ["yes" if glob_match("a*b", t) else "no" for t in ("aaab", "aac")]
    print(" ".join(results))


if __name__ == "__main__":
    main()
