from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

def find_next(sx, sy):
    limit = grid[sx][sy]
    visited = [[False] * n for _ in range(n)]   # 매번 새로
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    best = None

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] < limit:
                visited[nx][ny] = True
                q.append((nx, ny))
                cand = (-grid[nx][ny], nx, ny)
                if best is None or cand < best:
                    best = cand

    if best is None:
        return None
    return best[1], best[2]

for _ in range(k):
    nxt = find_next(r, c)
    if nxt is None:
        break
    r, c = nxt

print(r + 1, c + 1)