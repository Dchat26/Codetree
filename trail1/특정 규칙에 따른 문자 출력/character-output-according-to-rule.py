a = int(input().rstrip())

cnt = 1
for i in range(2 * a - 1):
    if i < a - 1:
        print(' ' * (2 * (a - cnt)), end='')
        print(" ".join('@' * cnt), end='')
        print()

        cnt += 1
    else:
        print(" ".join('@' * cnt), end='')
        print(' ' * (2 * (a - cnt)), end='')
        print()

        cnt -= 1