a = int(input().rstrip())

for i in range(a, 0, -1):
    print('*' * i, end='')
    print(' ' * (2 * (a - i)), end='')
    print('*' * i)