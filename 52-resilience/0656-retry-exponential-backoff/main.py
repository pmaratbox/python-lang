from tenacity import Retrying, stop_after_attempt, wait_exponential

# Scripted failure sequence driven by a shared counter: the operation fails on
# the first three attempts, then succeeds. tenacity retries it with an
# exponential backoff strategy (zero base delay so the run stays deterministic).
n = {"v": 0}


def op():
    n["v"] += 1
    if n["v"] < 4:
        raise ValueError("fail")
    return "done"


Retrying(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=0),
    reraise=True,
)(op)

print(n["v"])  # total attempts -> 4
