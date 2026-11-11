import sys

a = int(input().rstrip())
alist = list(map(int, input().split()))

answer = sys.maxsize
for i in range(a):
    alist[i] *= 2

    for j in range(a):
        arr = [k for idx, k in enumerate(alist) if idx != j]

        score = 0
        for l in range(a - 2):
            score += abs(arr[l] - arr[l+1])
        
        answer = min(answer, score)
    
    alist[i] //= 2

print(answer)