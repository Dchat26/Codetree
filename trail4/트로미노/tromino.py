n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

s = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

answer = 0
for i in range(n):
    for j in range(m - 2):
        temp = sum(grid[i][j+k] for k in range(3))
        answer = max(answer, temp)

for i in range(n - 2):
    for j in range(m):
        temp = sum(grid[i+k][j] for k in range(3))
        answer = max(answer, temp)

for i in range(n):
    for j in range(m):
        for a, b in s:
            if 0 <= i + a < n and 0 <= j + b < m:
                temp = grid[i][j]
                temp += grid[i+a][j]
                temp += grid[i][j+b]
        
                answer = max(answer, temp)

print(answer)