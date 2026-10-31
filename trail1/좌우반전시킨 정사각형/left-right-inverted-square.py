a = int(input().rstrip())

for i in range(1, a + 1):
    for j in range(a, 0, -1):
        print(i * j, end=' ')
    print()