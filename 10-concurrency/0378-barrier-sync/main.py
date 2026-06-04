import threading

reached = 0
lock = threading.Lock()
barrier = threading.Barrier(3)


def worker():
    global reached
    with lock:
        reached += 1
    barrier.wait()


threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("all reached: {}".format(reached))
