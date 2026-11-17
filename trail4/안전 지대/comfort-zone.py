import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
mx = max(max(row) for row in grid)


def dfs(x, y, h, t):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and t[nx][ny] > h:
            t[nx][ny] = -1
            dfs(nx, ny, h, t)


answer = 0
best_k = 1
for h in range(1, mx + 1):
    cnt = 0
    temp = [row[:] for row in grid]  
    for i in range(n):
        for j in range(m):
            if temp[i][j] > h:
                cnt += 1
                temp[i][j] = -1   
                dfs(i, j, h, temp)
    if cnt > answer:
        answer = cnt
        best_k = h

print(best_k, answer)