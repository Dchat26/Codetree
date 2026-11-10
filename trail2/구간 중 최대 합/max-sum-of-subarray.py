import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = -sys.maxsize
for i in range(n - k + 1):
    temp = 0
    for j in range(k):
        temp += arr[i+j]
    
    answer = max(answer, temp)

print(answer)