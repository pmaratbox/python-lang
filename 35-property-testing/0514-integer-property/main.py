# hypothesis — a property over generated integers, run programmatically
from hypothesis import given, strategies as st, settings


@settings(max_examples=100)
@given(st.integers(), st.integers())
def prop(a, b):
    assert a + b == b + a


prop()
print("passed")
