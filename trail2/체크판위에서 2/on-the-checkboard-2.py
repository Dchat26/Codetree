a, b = map(int, input().split())
board = [input().split() for _ in range(a)]

answer = 0

for x1 in range(1, a - 1):
    for y1 in range(1, b - 1):
        if board[0][0] == board[x1][y1]:
            continue

        for x2 in range(x1 + 1, a - 1):
            for y2 in range(y1 + 1, b - 1):
                if board[x1][y1] == board[x2][y2]:
                    continue

                if board[x2][y2] == board[a-1][b-1]:
                    continue

                answer += 1

print(answer)