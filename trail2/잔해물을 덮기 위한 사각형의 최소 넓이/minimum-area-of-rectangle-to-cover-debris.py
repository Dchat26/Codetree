alist = [tuple(map(int, input().split())) for _ in range(2)]

offset = min(0, min(j for i in alist for j in i))

row, col = 0, 0

for a, b, c, d in alist:
    a, b, c, d = a - offset, b - offset, c - offset, d - offset

    row = max(row, a, c)
    col = max(col, b, d)

answer = [[0] * col for _ in range(row)]

for idx, (a, b, c, d) in enumerate(alist):
    a, b, c, d = a - offset, b - offset, c - offset, d - offset

    for i in range(a, c):
        for j in range(b, d):
            if idx == 0:
                answer[i][j] = 1
            else:
                answer[i][j] = 0

if sum(j for i in answer for j in i) == 0:
    print(0)
else:
    x1, x2 = row, 0
    y1, y2 = col, 0
    for i in range(row):
        for j in range(col):
            if answer[i][j] == 1:
                x1 = min(x1, i)
                x2 = max(x2, i + 1)
                y1 = min(y1, j)
                y2 = max(y2, j + 1)

    print((x2 - x1) * (y2 - y1))