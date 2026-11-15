from collections import deque

n = int(input().rstrip())
q = deque()
for _ in range(n):
    a = input().split()

    if len(a) == 2:
        b, c = a
        c = int(c)
        if b == "push_front":
            q.appendleft(c)
        else:
            q.append(c)
    else:
        if a[0] == "pop_front":
            print(q.popleft())
        elif a[0] == "pop_back":
            print(q.pop())
        elif a[0] == "size":
            print(len(q))
        elif a[0] == "empty":
            print(0 if q else 1)
        elif a[0] == "front":
            print(q[0])
        else:
            print(q[-1])