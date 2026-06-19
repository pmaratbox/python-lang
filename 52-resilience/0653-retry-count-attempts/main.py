from tenacity import Retrying, stop_after_attempt, wait_none

# Shared counter incremented on every attempt of the scripted operation.
attempts = {"v": 0}


def always_fails():
    attempts["v"] += 1
    raise ValueError("scripted failure")


# Up to 5 total attempts, no delay between them. The operation always raises,
# so tenacity retries until the stop condition is hit, then re-raises.
retry = Retrying(stop=stop_after_attempt(5), wait=wait_none(), reraise=True)
try:
    retry(always_fails)
except ValueError:
    pass

print(attempts["v"])
