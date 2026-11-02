a = int(input().rstrip())

answer = [[0] * a for _ in range(a)]

for i in range(a):
    answer[i][0] = 1
    answer[i][i] = 1

for i in range(a):
    for j in range(a):
        dx = i - 1
        dy = j - 1
        if 0 <= dx and dx < a and 0 <= dy and dy < a:
            answer[i][j] = answer[dx][dy] + answer[dx][j]

for i in answer:
    for j in i:
        if j != 0:
            print(j, end=' ')
    print()