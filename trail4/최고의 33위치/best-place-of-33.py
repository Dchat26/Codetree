a = int(input().rstrip())
alist = [list(map(int, input().split())) for _ in range(a)]

answer = 0
for i in range(a - 2):
    for j in range(a - 2):
        temp = 0
        for k in range(3):
            for l in range(3):
                nx, ny = i + k, j + l
                if 0 <= nx < a and 0 <= ny < a:
                    temp += alist[nx][ny]
        
        answer = max(answer, temp)

print(answer)