a = int(input().rstrip())

answer = [[0] * a for _ in range(a)]

for i in range(a):
    for j in range(a):
        answer[i][j] = j * a + i + 1

for i in answer:
    print(*i)