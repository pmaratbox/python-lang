from parsy import string

# Alternative / choice combinator: `|` tries the left parser first,
# and falls back to the right parser if the left one fails.
# Here the parser accepts the literal "cat" OR the literal "dog".
animal = string("cat") | string("dog")

result = animal.parse("dog")
print(result)
