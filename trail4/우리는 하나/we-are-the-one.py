from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
idx = [(i, j) for i in range(n) for j in range(n)]

def bfs(starts):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for x, y in starts:
        visited[x][y] = True 
        q.append((x, y))

    cnt = len(starts)
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(town[x][y] - town[nx][ny])
                if u <= diff <= d:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    return cnt

answer = 0
for picked in combinations(idx, k):
    answer = max(answer, bfs(picked))

print(answer)