def counts(text):
    words = len(text.split())
    lines = len(text.split("\n"))
    chars = len(text)
    return words, lines, chars


text = "a b\nc"
print("{} {} {}".format(*counts(text)))
