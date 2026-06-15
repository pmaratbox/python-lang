from parsy import regex

# `regex(r'\s*')` is a combinator matching optional whitespace.
whitespace = regex(r'\s*')

# `regex(r'[0-9]+')` matches a digit-run; `.map(int)` turns it into an int.
integer = regex(r'[0-9]+').map(int).desc('integer')

# `whitespace >> integer << whitespace` sequences the parsers, discarding the
# leading and trailing whitespace and keeping only the integer.
padded = whitespace >> integer << whitespace

print(padded.parse('  42  '))
