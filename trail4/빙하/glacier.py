from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def find_melting():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([(0, 0)])
    melt = []

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    melt.append((nx, ny))
    return melt


time = 0
last = 0
while True:
    melt = find_melting()
    if not melt:
        break
    for x, y in melt:
        grid[x][y] = 0
    time += 1
    last = len(melt)

print(time, last)