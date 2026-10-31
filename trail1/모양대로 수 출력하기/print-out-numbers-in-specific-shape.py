a = int(input().rstrip())

for i in range(a, 0, -1):
    print('  ' * (a - i), end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
