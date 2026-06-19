from tenacity import Retrying, stop_after_attempt, wait_none, retry_if_result

counter = {"v": 0}


def grow():
    counter["v"] += 1
    return counter["v"]


# Retry while the RETURNED value is < 3 (result-predicate, not exception-based).
# grow() returns 1, then 2 (both retried), then 3 which the predicate accepts.
result = Retrying(
    stop=stop_after_attempt(10),
    wait=wait_none(),
    retry=retry_if_result(lambda v: v < 3),
)(grow)

print(result)
