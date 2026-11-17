n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    global cnt
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            grid[nx][ny] = 0
            cnt += 1
            dfs(nx, ny)

answer = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            grid[i][j] = 0        # 시작 칸도 방문 처리
            cnt = 1               # 시작 칸 포함
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for a in answer:
    print(a)