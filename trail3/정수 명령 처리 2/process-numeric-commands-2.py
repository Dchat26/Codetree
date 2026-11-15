from collections import deque

n = int(input().rstrip())

q = deque()
for _ in range(n):
    a = input().split()
    if len(a) == 2:
        b, c = a
        c = int(c)
        q.appendleft(c)
    else:
        if a[0] == "pop":
            print(q.pop())
        elif a[0] == "size":
            print(len(q))
        elif a[0] == "empty":
            print(0 if q else 1)
        else:
            print(q[-1])