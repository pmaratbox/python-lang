from hypothesis import given, strategies as st, settings

# Property over TWO generated integer arguments a and b: the max of the pair
# is at least as large as each input. Each @given strategy maps to a parameter,
# so Hypothesis draws a fresh (a, b) pair for every example.
@settings(max_examples=100)
@given(st.integers(), st.integers())
def prop(a, b):
    assert max(a, b) >= a
    assert max(a, b) >= b

# Run the property programmatically; if no AssertionError, it held for all generated pairs.
prop()
print("passed")
