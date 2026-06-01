stack = []
for n in [1, 2, 3]:
    stack.append(n)

popped = []
while stack:
    popped.append(stack.pop())

print(*popped)
