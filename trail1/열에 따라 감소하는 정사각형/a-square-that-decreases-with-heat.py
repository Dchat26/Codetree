a = int(input().rstrip())

for _ in range(a):
    for i in range(a, 0, -1):
        print(i, end=' ')
    print()