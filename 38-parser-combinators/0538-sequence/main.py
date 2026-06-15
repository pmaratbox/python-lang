from parsy import string, seq

# Sequence two parsers: char 'a' THEN char 'b'.
# `seq` runs the parsers in order and collects their results into a list;
# `.map` then joins the two characters into a single string.
parser = seq(string("a"), string("b")).map("".join)

print(parser.parse("ab"))
