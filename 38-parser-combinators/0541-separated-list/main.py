from parsy import regex, string

# `regex(r'[0-9]+').map(int)` is the integer combinator.
integer = regex(r'[0-9]+').map(int).desc('integer')

# `.sep_by(separator)` is the combinator that parses zero-or-more `integer`
# values separated by the `,` literal, collecting them into a list.
csv_ints = integer.sep_by(string(','))

# Run the parser on the fixed input, then sum the parsed list.
values = csv_ints.parse('1,2,3')
print(sum(values))
