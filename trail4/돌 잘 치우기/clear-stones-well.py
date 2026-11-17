from itertools import combinations
from collections import deque

n, k, m = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
klist = [tuple(map(int, input().split())) for _ in range(k)]
stone = [(i, j) for i in range(n) for j in range(n) if nlist[i][j] == 1]


def bfs():
    global cnt

    visited = [[False] * n for _ in range(n)]
    for x, y in klist:
        x, y = x - 1, y - 1
        if visited[x][y] == False and nlist[x][y] == 0:
            cnt += 1
            visited[x][y] = True
            
        q = deque([(x, y)])
        while q:
            a, b = q.popleft()

            for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nx, ny = a + dx, b + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and nlist[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))


answer = 0
for i in combinations(stone, m):
    for x, y in i:
        nlist[x][y] = 0
    
    cnt = 0
    bfs()
    answer = max(answer, cnt)

    for x, y in i:
        nlist[x][y] = 1
    
print(answer)