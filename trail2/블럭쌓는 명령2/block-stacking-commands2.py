a, b = map(int, input().split())

alist = [0] * (a + 1)
for _ in range(b):
    c, d = map(int, input().split())
    for i in range(c, d + 1):
        alist[i] += 1

print(max(alist))