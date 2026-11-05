a = int(input().rstrip())

result = []
for i in range(1, a + 1):
    a, b = map(int, input().split())

    result.append((a, b, i))

result.sort(key=lambda x: (abs(x[0]) + abs(x[1])))

for i in result:
    print(i[2])