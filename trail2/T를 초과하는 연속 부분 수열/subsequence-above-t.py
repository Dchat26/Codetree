a, b = map(int, input().split())
alist = list(map(int, input().split()))

answer = 0
temp = 0
for i in range(a):
    if alist[i] > b:
        temp += 1
    else:
        answer = max(answer, temp)
        temp = 0

answer = max(answer, temp)

print(answer)