from tenacity import Retrying, stop_after_attempt, wait_none

# Scripted failure sequence: the operation ALWAYS fails. A shared counter
# records how many times tenacity actually invokes it.
attempts = {"v": 0}


def always_fails():
    attempts["v"] += 1
    raise ValueError("scripted failure")


# Allow 3 total attempts (2 retries). reraise=True surfaces the last
# exception once the stop condition is reached.
try:
    Retrying(stop=stop_after_attempt(3), wait=wait_none(), reraise=True)(always_fails)
except ValueError:
    print("failed")
