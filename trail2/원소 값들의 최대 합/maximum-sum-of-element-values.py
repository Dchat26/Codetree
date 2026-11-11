a, b = map(int, input().split())
alist = list(map(int, input().split()))

answer = 0
for i in range(a):
    temp = 0
    p = i
    for _ in range(b):
        temp += alist[p]
        p = alist[p] - 1
    
    answer = max(answer, temp)

print(answer)