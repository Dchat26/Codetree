a = int(input().rstrip())
alist = list(map(int, input().split()))

alist.sort()

answer = 0
for i in range(a):
    answer = max(answer, alist[i] + alist[-(i+1)])

print(answer)