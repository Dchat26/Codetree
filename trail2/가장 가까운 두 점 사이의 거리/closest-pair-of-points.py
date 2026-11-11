import sys

a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = sys.maxsize
for i in range(a - 1):
    for j in range(i + 1, a):
        x, y = alist[i]
        x2, y2 = alist[j]

        answer = min(answer, (x - x2) ** 2 + (y - y2) ** 2)

print(answer)