a = int(input().rstrip())
alist = [input().split() for _ in range(a)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
adict = {"E": 0, "W": 1, "S": 2, "N": 3}

answer = -1
x, y = 0, 0
p = 0
for a, b in alist:
    b = int(b)
    is_TF = False
    for _ in range(b):
        x += dx[adict[a]]
        y += dy[adict[a]]

        p += 1

        if x == 0 and y == 0:
            is_TF = True
            break
    
    if is_TF:
        answer = p
        break

print(answer)