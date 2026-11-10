n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i, n):
        t = []
        for k in range(i, j + 1):
            t.append(arr[k])

        total = sum(t)
        if total % len(t) == 0:
            if total // len(t) in t:
                answer += 1

print(answer)