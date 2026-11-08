N, T = map(int, input().split())
str = input().rstrip()
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pos = 0
x, y = N // 2, N // 2
answer = board[N // 2][N // 2]
for i in str:
    if i == "F":
        nx = x + dx[pos]
        ny = y + dy[pos]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            answer += board[x][y]
    elif i == "R":
        pos = (pos + 1) % 4
    else:
        pos = (pos + 3) % 4

print(answer)