from collections import deque

queue = deque()
for n in (1, 2, 3):
    queue.append(n)

items = []
while queue:
    items.append(str(queue.popleft()))
print(" ".join(items))
