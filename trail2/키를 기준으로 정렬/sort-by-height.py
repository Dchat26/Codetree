a = int(input().rstrip())

result = []
for _ in range(a):
    result.append(tuple(input().split()))

result.sort(key=lambda x: x[1])

for i in result:
    print(*i)