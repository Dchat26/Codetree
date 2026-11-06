a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]
offset = min(0, min(j for i in alist for j in i))

row, col = 0, 0
for a, b, c, d in alist:
    a, b, c, d = a - offset, b - offset, c - offset, d - offset

    row = max(row, a, c)
    col = max(col, b, d)

answer = [[""] * col for _ in range(row)]
for idx, (a, b, c, d) in enumerate(alist):
    a, b, c, d = a - offset, b - offset, c - offset, d - offset

    p = "R"
    if idx % 2 == 0:
        p = "R"
    else:
        p = "B"

    for i in range(a, c):
        for j in range(b, d):
            answer[i][j] = p

print(sum(1 for i in answer for j in i if j == "B"))