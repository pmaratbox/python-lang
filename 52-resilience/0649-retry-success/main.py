from tenacity import Retrying, stop_after_attempt, wait_none

n = {"v": 0}                  # shared attempt counter


def op():
    n["v"] += 1               # count this attempt
    return "ok"               # succeeds on the very first call


# Retrying drives the call; no failure, so it runs exactly once.
Retrying(stop=stop_after_attempt(5), wait=wait_none(), reraise=True)(op)
print(n["v"])                 # attempt count from the library -> 1
