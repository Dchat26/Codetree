from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    global cnt

    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))


cnt = 0
for x, y in points:
    if visited[x-1][y-1] == False and grid[x-1][y-1] == 0:
        visited[x-1][y-1] = True
        cnt += 1
        bfs(x-1, y-1)

print(cnt)