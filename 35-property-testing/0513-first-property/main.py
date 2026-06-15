# 0513 — First property: reversing a list twice yields the original.
from hypothesis import given, strategies as st, settings


@settings(max_examples=100)
@given(st.lists(st.integers()))
def prop_reverse_twice(xs):
    assert list(reversed(list(reversed(xs)))) == xs


# Run the property programmatically (not via a test runner).
# Hypothesis generates ~100 integer lists; if none falsify it, no AssertionError is raised.
prop_reverse_twice()
print("passed")
