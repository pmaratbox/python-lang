from parsy import regex

# `regex(r'[0-9]+')` matches a run of digits; the first `.map(int)`
# transforms the matched text into a Python int, and a second
# `.map(...)` transforms that integer to value * 2.
doubled = regex(r'[0-9]+').map(int).map(lambda n: n * 2).desc('doubled integer')

print(doubled.parse('21'))
