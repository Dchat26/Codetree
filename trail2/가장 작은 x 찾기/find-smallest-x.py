a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

c, d = alist[0]

answer = 0
for i in range(c // 2, d // 2 + 1):
    is_TF = True
    for idx, j in enumerate(alist):
        c1, d1 = j
        if not c1 <= i * (2 ** (idx + 1)) <= d1:
            is_TF = False
            break
    
    if is_TF:
        answer = i
        break

print(answer)