from itertools import combinations

a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]
s = max(i for _, i in alist)

line = [0] * (s + 1)
for x, y in alist:
    for i in range(x, y + 1):
        line[i] += 1

answer = 0
for i, j, k in combinations(alist, 3):
    temp = line.copy()
    for a, b in (i, j, k):
        for l in range(a, b + 1):
            temp[l] -= 1
    
    is_TF = True
    for m in temp:
        if not (m == 1 or m == 0):
            is_TF = False
            break
    
    if is_TF:
        answer += 1

print(answer)