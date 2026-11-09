import sys

a = int(input().rstrip())
alist = [list(map(int, input().split())) for _ in range(a)]

max_val = -sys.maxsize
for i in range(a):
    for j in range(a - 2):
        p = alist[i][j] + alist[i][j+1] + alist[i][j+2]

        max_val = max(max_val, p)

print(max_val)