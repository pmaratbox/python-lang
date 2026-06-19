from tenacity import Retrying, stop_after_attempt, wait_none

# scripted failure sequence: fail once, then return the string "ok"
counter = {"v": 0}


def op():
    counter["v"] += 1
    if counter["v"] < 2:
        raise ValueError("transient failure")
    return "ok"


# tenacity drives the retries; the call returns the successful result
result = Retrying(stop=stop_after_attempt(5), wait=wait_none(), reraise=True)(op)
print(result)  # "ok"
