a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = 0
for i in range(1, 11):
    cur = -1
    cnt = 0
    for p, x in alist:
        if p == i:
            if cur != -1 and cur != x:
                cnt += 1
                cur = x
            else:
                cur = x
    
    answer += cnt

print(answer)