s = input().rstrip()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sdict = {"L": -1, "R": 1}

x, y = 0, 0
dxy = 0
for i in s:
    if i == "F":
        nx = dx[((dxy + 4) % 4)]
        ny = dy[((dxy + 4) % 4)]

        x += nx
        y += ny
    else:
        dxy += sdict[i]

print(x, y) 