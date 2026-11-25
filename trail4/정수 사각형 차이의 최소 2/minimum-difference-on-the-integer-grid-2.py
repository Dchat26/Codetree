INF = float('inf')

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = INF
for lo in range(1, 101):
    if lo > min(grid[0][0], grid[n-1][n-1]):
        break

    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lo:
                continue
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                best = INF
                if i > 0:
                    best = min(best, dp[i-1][j])
                if j > 0:
                    best = min(best, dp[i][j-1])
                if best < INF:
                    dp[i][j] = max(best, grid[i][j])

    if dp[n-1][n-1] < INF:
        ans = min(ans, dp[n-1][n-1] - lo)

print(ans)