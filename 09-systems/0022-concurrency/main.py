from concurrent.futures import ThreadPoolExecutor

def task(x: int) -> int:
    return x

with ThreadPoolExecutor() as pool:
    a = pool.submit(task, 1)
    b = pool.submit(task, 2)
    print(f"sum: {a.result() + b.result()}")
