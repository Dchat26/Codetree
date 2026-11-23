n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    nx, ny = r, c
    for i in range(grid[r][c] - 1):
        nx, ny = nx + x, ny + y
        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] = 0
        else:
            break

grid[r][c] = 0
answer = []
for i in range(n):
    temp = []
    for j in range(n - 1, -1, -1):
        if grid[j][i] != 0:
            temp.append(grid[j][i])
        
    if len(temp) < n:
        while len(temp) < n:
            temp.append(0)

    answer.append(temp)

for i in range(n - 1, -1, -1):
    for j in range(n):
        print(answer[j][i], end=' ')
    print()