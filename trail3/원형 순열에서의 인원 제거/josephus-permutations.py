from collections import deque

a, b = map(int, input().split())
alist = deque([i for i in range(1, a + 1)])

while alist:
    for _ in range(b - 1):
        alist.append(alist.popleft())
    print(alist.popleft(), end=' ')