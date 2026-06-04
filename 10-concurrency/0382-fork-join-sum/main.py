from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=8)


def fork_sum(lo, hi):
    if hi - lo <= 1:
        return lo
    mid = (lo + hi) // 2
    left = pool.submit(fork_sum, lo, mid)
    right = pool.submit(fork_sum, mid, hi)
    return left.result() + right.result()


total = fork_sum(1, 9)
pool.shutdown()
print(total)
