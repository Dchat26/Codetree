a = int(input().rstrip())

cnt = 1
for i in range(2 * a - 1):
    print(' ' * (a - cnt), end='')
    print('*' * (2 * cnt - 1), end='')
    print(' ' * (a - cnt), end='')
    print()

    if i < a - 1:
        cnt += 1
    else:
        cnt -= 1