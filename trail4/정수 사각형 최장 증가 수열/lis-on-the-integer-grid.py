n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

cells = sorted((grid[i][j], i, j) for i in range(n) for j in range(n))

for v, x, y in cells:
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] < v:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

print(max(map(max, dp)))