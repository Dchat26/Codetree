n, m = map(int, input().split())
arr = list(map(int, input().split()))

p = -1
answer = 0
for idx, i in enumerate(arr):
    if idx > p and i == 1:
        p = idx + 2 * m
        answer += 1

print(answer)