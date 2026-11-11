from itertools import combinations

a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = 0
for i, j, k in combinations(alist, 3):
    x, y = i
    x2, y2 = j
    x3, y3 = k

    dx, dy = 0, 0
    if x == x2:
        dy = abs(y - y2)
    elif x == x3:
        dy = abs(y - y3)
    elif x2 == x3:
        dy = abs(y2 - y3)
    
    if y == y2:
        dx = abs(x - x2)
    elif y == y3:
        dx = abs(x - x3)
    elif y2 == y3:
        dx = abs(x2 - x3)
    
    if dx and dy:
        answer = max(answer, (dx * dy / 2) * 2)

print(int(answer))