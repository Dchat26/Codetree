a = int(input().rstrip())

result = []
for _ in range(a):
    a, b, c = input().split()
    b, c = map(int, (b, c))

    result.append((a, b, c))

result.sort(key=lambda x: (x[1], -x[2]))

for i in result:
    print(*i)