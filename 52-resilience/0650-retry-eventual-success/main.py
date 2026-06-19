from tenacity import Retrying, stop_after_attempt, wait_none

# Scripted failure sequence driven by a shared counter: the operation fails on
# the first attempt, then succeeds on the second.
attempts = {"v": 0}


def op():
    attempts["v"] += 1
    if attempts["v"] < 2:
        raise ValueError("transient failure")
    return "ok"


# tenacity drives the actual retrying; zero delay keeps the count deterministic.
Retrying(stop=stop_after_attempt(5), wait=wait_none(), reraise=True)(op)

# The total attempt count comes from the library actually retrying the op.
print(attempts["v"])
