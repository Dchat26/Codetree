N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

answer = 0
for i in range(N - 1):
    temp = 1
    for j in range(i + 1, N):
        if arr[j] - arr[i] <= K:
            temp += 1
        else:
            break
    
    answer = max(answer, temp)

print(answer)