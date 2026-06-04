from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=1) as pool:
    a = pool.submit(lambda: 5).result()
    b = pool.submit(lambda: a * 2).result()
    c = pool.submit(lambda: b + 1).result()

print(c)
