from parsy import string

# `string('a')` matches a single 'a'; `.many()` is the repetition
# combinator that applies it zero-or-more times, collecting a list.
many_a = string('a').many()

# Run the combinator on the fixed input and count the matches.
result = many_a.parse('aaaa')

print(len(result))
