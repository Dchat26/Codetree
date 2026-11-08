n = int(input().rstrip())
answer = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

x, y = n - 1, n - 1
pos = 0
for i in range(n * n, 0, -1):
    answer[x][y] = i

    for _ in range(4):
        nx = x + dx[pos]
        ny = y + dy[pos]
        if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
            x, y = nx, ny
            break
        else:
            pos = (pos + 1) % 4

for i in answer:
    print(*i)