import threading

value = 0
lock = threading.Lock()


def cas(expected, new):
    global value
    with lock:
        if value == expected:
            value = new
            return True
        return False


def worker():
    for _ in range(25):
        while True:
            cur = value
            if cas(cur, cur + 1):
                break


threads = [threading.Thread(target=worker) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(value)
