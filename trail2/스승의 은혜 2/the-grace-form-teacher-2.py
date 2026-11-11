n, m = map(int, input().split())
nlist = [int(input().rstrip()) for _ in range(n)]
nlist.sort()

answer = 0
for i in range(n):
    p = m
    temp = 0
    for idx, j in enumerate(nlist):
        if i == idx:
            p -= j // 2
        else:
            p -= j
        
        if p < 0:
            break
        else:
            temp += 1
    
    answer = max(answer, temp)

print(answer)