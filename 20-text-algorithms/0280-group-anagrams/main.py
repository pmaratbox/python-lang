from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())


print(len(group_anagrams(["eat", "tea", "tan", "ate", "nat"])))
