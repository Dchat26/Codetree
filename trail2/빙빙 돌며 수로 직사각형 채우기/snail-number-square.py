a, b = map(int, input().split())
board = [[0] * b for _ in range(a)]

dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

x, y = 0, 0
start = 0
for i in range(1, a * b + 1):
    board[x][y] = i

    if i == a * b:
        break

    while True:
        nx = x + dxs[start]
        ny = y + dys[start]

        if 0 <= nx and nx < a and 0 <= ny and ny < b and board[nx][ny] == 0:
            x, y = nx, ny
            break
        else:
            start = (start + 5) % 4

for i in board:
    print(*i)