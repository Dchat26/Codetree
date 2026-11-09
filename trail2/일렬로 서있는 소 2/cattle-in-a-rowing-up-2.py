a = int(input().rstrip())
alist = list(map(int, input().split()))

answer = 0
for i in range(len(alist) - 2):
    for j in range(i + 1, len(alist) - 1):
        for k in range(j + 1, len(alist)):
            if i < j and j < k and alist[i] <= alist[j] and alist[j] <= alist[k]:
                answer += 1

print(answer)