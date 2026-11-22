from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

if board[0][0] == 0:
    print(0)
else:
    visited[0][0] = True
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    print(1 if visited[n-1][m-1] else 0)
