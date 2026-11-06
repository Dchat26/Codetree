a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]
offset = min(0, min(j for i in alist for j in i))

row, col = 0, 0
for a, b in alist:
    a, b = a - offset + 8, b - offset + 8
    row = max(row, a)
    col = max(col, b)

answer = [[0] * col for _ in range(row)]
for a, b in alist:
    a, b = a - offset, b - offset
    for i in range(a, a + 8):
        for j in range(b, b + 8):
            answer[i][j] = 1

print(sum(j for i in answer for j in i))