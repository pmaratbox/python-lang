def main():
    inner = ValueError("inner")
    try:
        raise RuntimeError("outer") from inner
    except RuntimeError as outer:
        print("{}: {}".format(outer, outer.__cause__))


if __name__ == "__main__":
    main()
