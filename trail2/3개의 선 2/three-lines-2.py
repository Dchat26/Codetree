from itertools import combinations

a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

board = [[0] * 11 for _ in range(11)]

for x, y in alist:
    board[x][y] = 1

row = [sum(board[i]) for i in range(11)]
col = [sum(board[i][j] for i in range(11)) for j in range(11)]

total = sum(row)
answer = 0

# 가로 3
for i, j, k in combinations(range(11), 3):
    if row[i] + row[j] + row[k] == total:
        answer = 1
        break

# 세로 3
if not answer:
    for i, j, k in combinations(range(11), 3):
        if col[i] + col[j] + col[k] == total:
            answer = 1
            break

# 가로 2 + 세로 1
if not answer:
    for i, j in combinations(range(11), 2):
        for k in range(11):
            temp = row[i] + row[j] + col[k]
            temp -= board[i][k] + board[j][k]

            if temp == total:
                answer = 1
                break

        if answer:
            break

# 가로 1 + 세로 2
if not answer:
    for i, j in combinations(range(11), 2):
        for k in range(11):
            temp = col[i] + col[j] + row[k]
            temp -= board[k][i] + board[k][j]

            if temp == total:
                answer = 1
                break

        if answer:
            break

print(answer)