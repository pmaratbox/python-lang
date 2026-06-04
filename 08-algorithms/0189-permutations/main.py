from itertools import permutations


if __name__ == "__main__":
    for perm in permutations([1, 2, 3]):
        print(" ".join(str(x) for x in perm))
