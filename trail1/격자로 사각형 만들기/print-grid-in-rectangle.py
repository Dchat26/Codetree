a = int(input().rstrip())

answer = [[0] * a for _ in range(a)]

for i in range(a):
    answer[i][0], answer[0][i] = 1, 1

for i in range(a):
    for j in range(a):
        dx = i - 1
        dy = j - 1
        if 0 <= dx and dx < a and 0 <= dy and dy < a:
            answer[i][j] = answer[dx][j] + answer[i][dy] + answer[dx][dy]
    
for i in answer:
    print(*i)