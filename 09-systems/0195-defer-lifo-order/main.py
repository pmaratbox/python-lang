def main():
    deferred = []
    for n in (1, 2, 3):
        deferred.append(n)
    # run in last-in-first-out order
    print(" ".join(str(n) for n in reversed(deferred)))


if __name__ == "__main__":
    main()
