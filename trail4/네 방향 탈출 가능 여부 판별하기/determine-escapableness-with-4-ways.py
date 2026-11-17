from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
q = deque([(0, 0)])


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and a[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))


visited[0][0] = True
bfs()

print(1 if visited[n-1][m-1] else 0)