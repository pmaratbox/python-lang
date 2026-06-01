from collections import Counter

word = "banana"
counts = Counter(word)

print(" ".join(f"{ch}:{counts[ch]}" for ch in sorted(counts)))
