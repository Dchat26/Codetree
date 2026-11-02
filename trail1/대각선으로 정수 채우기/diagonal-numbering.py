a, b = map(int, input().split())

answer = [[0] * b for _ in range(a)]

num = 1
for i in range(a + b - 1):
    if i < b:
        x, y = 0, i
    else:
        x, y = i - b + 1, b - 1

    while True:
        answer[x][y] = num
        num += 1

        dx = x + 1
        dy = y - 1
        if 0 <= dx and dx < a and 0 <= dy and dy < b:
            x = dx
            y = dy
        else:
            break

for i in answer:
    print(*i)