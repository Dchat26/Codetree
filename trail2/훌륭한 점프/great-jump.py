n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = arr[0]
idx = 0
while idx < n:
    p = idx
    temp = float('inf')

    for i in range(idx + 1, min(idx + k + 1, n)):
        if temp > arr[i]:
            temp = arr[i]
            p = i

    if p == n - 1:
        break

    answer = max(answer, temp)
    idx = p

answer = max(answer, arr[n-1])

print(answer)