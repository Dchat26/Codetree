from collections import deque
from itertools import combinations

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

idx = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
answer = -1
for i in combinations(idx, k):
    temp = [j[:] for j in grid]
    for a, b in i:
        temp[a][b] = 0

    visited = [[False] * n for _ in range(n)]
    step = [[0] * n for _ in range(n)]

    q = deque([(r1, c1)])
    visited[r1][c1] = True
    is_TF = False
    while q and not is_TF:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and temp[nx][ny] != 1:
                if nx == r2 and ny == c2:
                    if answer != -1:
                        answer = min(answer, step[x][y] + 1)
                    else:
                        answer = step[x][y] + 1
                    
                    is_TF = True
                    break
                
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

if r1 == r2 and c1 == c2:
    print(0)
else:
    print(answer)