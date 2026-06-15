from parsy import regex

# `regex(r'[0-9]+')` is a combinator that matches one-or-more digits;
# `.map(int)` transforms the matched text into a Python int.
integer = regex(r'[0-9]+').map(int).desc('integer')

print(integer.parse('42'))
