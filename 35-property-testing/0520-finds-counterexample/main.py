# hypothesis finds a counterexample for a densely false property.
# Output suppression keeps hypothesis's falsifying-example/shrink report
# off stdout so only "found" is printed.
from hypothesis import given, strategies as st
import io
import contextlib


# A FALSE property: "every non-negative integer is < 100".
# Hypothesis generates inputs and will find a counterexample (n >= 100).
@given(st.integers(min_value=0, max_value=10 ** 6))
def every_nonneg_under_100(n):
    assert n < 100


buf = io.StringIO()
failed = False
try:
    # Suppress hypothesis's falsifying-example / shrink report.
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        every_nonneg_under_100()
except AssertionError:
    failed = True

print("found" if failed else "no-ce")
