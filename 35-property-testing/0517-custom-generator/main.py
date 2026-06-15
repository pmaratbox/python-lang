from hypothesis import given, strategies as st, settings

# Build a CUSTOM generator using the library's `map` combinator:
# take arbitrary integers and transform each into an even integer (n -> n*2).
even_integers = st.integers().map(lambda n: n * 2)

# Property: every value produced by the custom generator is even.
@settings(max_examples=100)
@given(even_integers)
def prop(n):
    assert n % 2 == 0

# Run the property programmatically; if no AssertionError, it held for all generated inputs.
prop()
print("passed")
