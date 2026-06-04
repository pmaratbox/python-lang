from concurrent.futures import ThreadPoolExecutor

nums = [1, 2, 3, 4]

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(lambda x: x * x, nums))

print(" ".join(str(r) for r in results))
