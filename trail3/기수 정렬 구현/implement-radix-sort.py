n = int(input())
arr = list(map(int, input().split()))

exp = 1
while max(arr) // exp > 0:
    bucket = [[] for _ in range(10)]
    for num in arr:
        digit = (num // exp) % 10
        bucket[digit].append(num)

    arr = []
    for b in bucket:
        arr.extend(b)

    exp *= 10

print(*arr)