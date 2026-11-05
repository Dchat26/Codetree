a = int(input().rstrip())

result = []
for _ in range(a):
    a, b, c, d = input().split()
    b, c, d = map(int, (b, c, d))

    result.append((a, b, c, d))

result.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in result:
    print(*i)