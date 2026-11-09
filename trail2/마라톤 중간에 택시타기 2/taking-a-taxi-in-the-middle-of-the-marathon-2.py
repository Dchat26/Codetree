import sys

a = int(input().rstrip())
alist = [list(map(int, input().split())) for _ in range(a)]

min_val = sys.maxsize
p = 1
while p < a - 1:
    total = 0
    x, y = alist[0][0], alist[0][1]
    for i in range(1, len(alist)):
        if i == p:
            continue
        
        x2, y2 = alist[i][0], alist[i][1]
        total += abs(x - x2) + abs(y - y2)
        x, y = x2, y2
    
    min_val = min(min_val, total)
    p += 1

print(min_val)