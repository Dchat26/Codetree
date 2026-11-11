a = int(input().rstrip())
alist = list(map(int, input().split()))
s = max(alist)

answer = 0
for i in range(1, s + 1):
    temp = 0
    for j in range(a - 1):
        for k in range(j + 1, a):
            if alist[j] - i == i - alist[k]:
                temp += 1
    
    answer = max(answer, temp)

print(answer)