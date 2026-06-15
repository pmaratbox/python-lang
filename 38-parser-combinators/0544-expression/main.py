from parsy import regex, string

# `regex(r'[0-9]+')` matches one-or-more digits; `.map(int)` turns the
# matched text into a Python int.
integer = regex(r'[0-9]+').map(int).desc('integer')

# `.sep_by(string('+'), min=1)` is the combinator that parses a list of
# integers separated by '+' signs. We `.map(sum)` to fold them together.
expression = integer.sep_by(string('+'), min=1).map(sum)

print(expression.parse('10+20+30'))
