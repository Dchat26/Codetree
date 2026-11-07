a = int(input().rstrip())
board = [tuple(map(int, input().split())) for _ in range(a)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

answer = 0
for i in range(a):
    for j in range(a):
        temp = 0
        for dx, dy in zip(dxs, dys):
            nx = i + dx
            ny = j + dy

            if 0 <= nx and nx < a and 0 <= ny and ny < a and board[nx][ny] == 1:
                temp += 1
        
        if temp >= 3:
            answer += 1

print(answer)