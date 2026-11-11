a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = 0
for x, x2 in alist:
    is_TF = True
    for x3, x4 in alist:
        if x == x3 and x2 == x4:
            continue
        
        if (x - x3) * (x2 - x4) < 0:
            is_TF = False
            break
    
    if is_TF:
        answer += 1

print(answer)