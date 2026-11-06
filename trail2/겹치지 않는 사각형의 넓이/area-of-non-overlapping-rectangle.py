alist = [tuple(map(int, input().split())) for _ in range(3)]
offset = min(0, min(j for i in alist for j in i))

row = 0
col = 0
for a, b, c, d in alist:
    a, b, c, d = a - offset, b - offset, c - offset, d - offset

    row = max(row, a, c)
    col = max(col, b, d)

answer = [[0] * col for _ in range(row)]
for idx, (a, b, c, d) in enumerate(alist):
    a, b, c, d = a - offset, b - offset, c - offset, d - offset
    m = 1
    if idx == 2:
        m = 2

    for i in range(a, c):
        for j in range(b, d):
            answer[i][j] += m

print(sum(j for i in answer for j in i if j == 1))