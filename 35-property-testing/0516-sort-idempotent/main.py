from hypothesis import given, strategies as st, settings


# Property: sorting an already-sorted list equals sorting once.
# sorted is idempotent, so this holds for every generated integer list.
@settings(max_examples=100)
@given(st.lists(st.integers()))
def sort_idempotent(xs):
    once = sorted(xs)
    assert sorted(once) == once


# Run the @given check programmatically; if no AssertionError, it passed.
sort_idempotent()
print("passed")
