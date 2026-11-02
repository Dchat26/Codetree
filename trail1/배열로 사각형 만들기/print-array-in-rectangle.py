answer = [[0] * 5 for _ in range(5)]

for i in range(5):
    answer[0][i], answer[i][0] = 1, 1

for i in range(5):
    for j in range(5):
        if i != 0 and j != 0:
            answer[i][j] = answer[i-1][j] + answer[i][j-1]

for i in answer:
    print(*i)