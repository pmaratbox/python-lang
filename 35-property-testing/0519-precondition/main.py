from hypothesis import given, assume, strategies as st, settings


@settings(max_examples=100)
@given(st.integers())
def prop(n):
    # Precondition: only test positive integers; assume() discards the rest.
    assume(n > 0)
    assert n + 1 > n


prop()
print("passed")
