a = int(input().rstrip())

cnt = a
for i in range(2 * a - 1):
    print(' ' * (2 * (a - cnt)), end='')
    print(" ".join('*' * (2 * cnt - 1)), end='')
    print(' ' * (2 * (a - cnt)), end='')
    print()

    if i < a - 1:
        cnt -= 1
    else:
        cnt += 1