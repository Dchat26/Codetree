from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

s = [[0] * n for _ in range(n)]
people = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 2]

for a, b in people:
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    step = [[0] * n for _ in range(n)]

    q = deque([(a, b)])
    found = False
    while q and not found:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 1:
                if grid[nx][ny] == 3:
                    s[a][b] = step[x][y] + 1
                    found = True
                    break
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

    if not found:
        s[a][b] = -1

for row in s:
    print(*row)