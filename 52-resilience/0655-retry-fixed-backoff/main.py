from tenacity import Retrying, stop_after_attempt, wait_fixed

# Scripted failure: the operation fails twice, then succeeds on the 3rd call.
counter = {"attempts": 0}


def op():
    counter["attempts"] += 1
    if counter["attempts"] < 3:
        raise ValueError("transient failure")
    return "done"


# Fixed backoff: a constant (zero) delay between attempts. The attempt count
# is delay-independent, so we keep the wait at zero to run instantly.
Retrying(stop=stop_after_attempt(5), wait=wait_fixed(0), reraise=True)(op)

print(counter["attempts"])
