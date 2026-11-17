n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and not visited[x][y]


def dfs(x, y):
    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


visited[0][0] = True
dfs(0, 0)
print(1 if visited[n-1][m-1] else 0)