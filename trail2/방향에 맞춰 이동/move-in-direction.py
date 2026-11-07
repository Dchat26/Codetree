a = int(input().rstrip())
alist = [input().split() for _ in range(a)]

adict = {"E": 0, "W": 1, "S": 2, "N": 3}
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0
for a, b in alist:
    b = int(b)

    nx = dx[adict[a]] * b
    ny = dy[adict[a]] * b

    x += nx
    y += ny

print(x, y)