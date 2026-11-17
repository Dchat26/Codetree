import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def dfs(x, y):
    global cnt

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
            visited[nx][ny] = True
            cnt += 1
            dfs(nx, ny)


answer = 0
mx = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            cnt = 1              
            dfs(i, j)

            if cnt >= 4:
                answer += 1
            mx = max(mx, cnt) 

print(answer, mx)