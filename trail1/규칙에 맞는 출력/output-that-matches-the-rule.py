a = int(input().rstrip())

for i in range(a, 0, -1):
    for j in range(a - i + 1):
        print(i + j, end=' ')
    print()