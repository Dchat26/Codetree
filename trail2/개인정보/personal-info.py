result = []
for _ in range(5):
    a, b, c = input().split()
    b = int(b)
    c = float(c)

    result.append((a, b, c))

result.sort(key=lambda x: x[0])
print("name")
for i in result:
    print(*i)
print()

result.sort(key=lambda x: -x[1])
print("height")
for i in result:
    print(*i)

