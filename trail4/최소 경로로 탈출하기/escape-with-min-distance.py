from collections import deque

n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
step = [[0] * m for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        if (a, b) == (n - 1, m - 1):
            return
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < m and c[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                step[nx][ny] = step[a][b] + 1
                q.append((nx, ny))


if c[0][0] == 1:
    bfs(0, 0)

print(step[n-1][m-1] if visited[n-1][m-1] else -1)