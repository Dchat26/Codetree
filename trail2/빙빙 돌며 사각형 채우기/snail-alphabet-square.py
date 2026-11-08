n, m = map(int, input().split())
answer = [[""] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
pos = 0
p = 65
for _ in range(n * m):
    answer[x][y] = chr(p)

    p += 1
    if p == 91:
        p = 65
    
    for _ in range(4):
        nx = x + dx[pos]
        ny = y + dy[pos]

        if 0 <= nx and nx < n and 0 <= ny and ny < m and answer[nx][ny] == "":
            x, y = nx, ny
            break
        else:
            pos = (pos + 1) % 4

for i in answer:
    print(*i)