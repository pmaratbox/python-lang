def majority_element(nums):
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 2, 3, 2]))
