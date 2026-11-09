import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = sys.maxsize
s = sum(arr)
for i in range(N - 1):
    for j in range(i + 1, N):
        a = arr[i] + arr[j]

        answer = min(answer, abs(S - (s - a)))

print(answer)