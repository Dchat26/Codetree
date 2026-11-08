n, m = map(int, input().split())

answer = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
pos = 0

for i in range(1, n * m + 1):
    answer[x][y] = i

    for _ in range(4):
        nx = x + dx[pos]
        ny = y + dy[pos]

        if 0 <= nx < n and 0 <= ny < m and answer[nx][ny] == 0:
            x, y = nx, ny
            break
        else:
            pos = (pos + 1) % 4

for i in answer:
    print(*i)