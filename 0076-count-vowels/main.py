word = "hello"
vowels = "aeiou"
count = sum(1 for ch in word if ch in vowels)
print(count)
