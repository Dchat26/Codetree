import sys

a = int(input().rstrip())
alist = list(map(int, input().split()))

answer = -sys.maxsize
for i in range(len(alist) - 1):
    for j in range(i + 1, len(alist)):
        if abs(i - j) >= 2:
            answer = max(answer, alist[i] + alist[j])

print(answer)