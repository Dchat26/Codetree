a = int(input().rstrip())

cnt = 1
for i in range(2 * a - 1):
    print(' ' * (a - cnt), end='')
    print(" ".join('*' * cnt))

    if i < a - 1:
        cnt += 1
    else:
        cnt -= 1