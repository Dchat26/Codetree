a, b = map(int, input().split())

answer = [[0] * (a + 1) for _ in range(a + 1)]

for i in range(1, b + 1):
    c, d = map(int, input().split())

    answer[c][d] = i

for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(answer[i][j], end=' ')
    print()