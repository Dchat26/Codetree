from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * n for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and grid[nx][ny] == 1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    row = []
    for j in range(n):
        if grid[i][j] == 0:
            row.append(-1)
        elif dist[i][j] == -1:
            row.append(-2)
        else:
            row.append(dist[i][j])
    print(*row)