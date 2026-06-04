import bisect


def lis_length(nums):
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def main():
    print(lis_length([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
