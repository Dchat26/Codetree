n = int(input())
arr = list(map(int, input().split()))

result = []
for idx, i in enumerate(arr):
    result.append(i)
    if idx % 2 == 0:
        print(sorted(result)[len(result) // 2], end=' ')