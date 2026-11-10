import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0
for i in range(T):
    temp += abs(arr[i] - H)

answer = temp

for i in range(T, N):
    temp -= abs(arr[i-T] - H)
    temp += abs(arr[i] - H)

    answer = min(answer, temp)

print(answer)