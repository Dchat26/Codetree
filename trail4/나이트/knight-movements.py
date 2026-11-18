from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 -1, c2 - 1
visited = [[False] * n for _ in range(n)]
s = [[0] * n for _ in range(n)]

q = deque([(r1, c1)])
while q:
    x, y = q.popleft()
    visited[x][y] = True
    if x == r2 and y == c2:
        break
    
    for dx, dy in ((-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            s[nx][ny] = s[x][y] + 1
            q.append((nx, ny))

if r1 == r2 and c1 == c2:
    print(0)
else:
    print(s[r2][c2] if s[r2][c2] else -1)