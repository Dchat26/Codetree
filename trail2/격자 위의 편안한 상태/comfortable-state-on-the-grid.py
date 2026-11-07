a, b = map(int, input().split())
board = [[0] * a for _ in range(a)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for _ in range(b):
    c, d = map(int, input().split())

    board[c-1][d-1] = 1

    temp = 0
    for i in range(4):
        nx = c + dxs[i] - 1
        ny = d + dys[i] - 1

        if 0 <= nx and nx < a and 0 <= ny and ny < a and board[nx][ny] == 1:
            temp += 1
    
    if temp == 3:
        print(1)
    else:
        print(0)