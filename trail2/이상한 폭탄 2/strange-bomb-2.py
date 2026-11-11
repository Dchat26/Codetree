N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

answer = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        if num[i] == num[j] and j - i <= K:
            answer = max(answer, num[i])

print(answer)