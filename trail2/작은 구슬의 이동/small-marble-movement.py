n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs = [1, 0, 0, -1]
dys = [0, -1, 1, 0]

ddict = {"U": 3, "D": 0, "R": 2, "L": 1}

x, y = r, c
pos = ddict[d]

for _ in range(t):
    nx = x + dxs[pos]
    ny = y + dys[pos]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny
    else:
        pos = 3 - pos

print(x, y)