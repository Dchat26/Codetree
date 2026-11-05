a = int(input().rstrip())

result = []
for i in range(1, a + 1):
    a, b = map(int, input().split())

    result.append((a, b, i))

result.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in result:
    print(*i)