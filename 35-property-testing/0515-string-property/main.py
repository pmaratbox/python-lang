from hypothesis import given, strategies as st, settings


# Property: the length of s+s equals 2*len(s) for any generated string s.
# Hypothesis's st.text() generates ~100 strings and feeds them to the check.
@settings(max_examples=100)
@given(st.text())
def prop_double_length(s):
    assert len(s + s) == 2 * len(s)


# Run the property programmatically (no test runner): calling the decorated
# function executes all generated examples. No AssertionError means it holds.
prop_double_length()
print("passed")
