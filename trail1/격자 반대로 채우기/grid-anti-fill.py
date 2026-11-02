a = int(input().rstrip())

answer = [[0] * a for _ in range(a)]

num = 1
x, y = a - 1, a - 1
for _ in range(a):
    if x == a - 1:
        while True:
            answer[x][y] = num
            num += 1

            x -= 1
            if x < 0:
                break
    else:
        while True:
            answer[x][y] = num
            num += 1

            x += 1
            if x == a:
                break
    
    if x == -1:
        x = 0
        y -= 1
    else:
        x = a - 1
        y -= 1

for i in answer:
    print(*i)