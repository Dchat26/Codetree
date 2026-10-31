a = int(input().rstrip())

for i in range(a):
    for j in range(i + 1):
        print((i + 1) * (j + 1), end=' ')
    print()