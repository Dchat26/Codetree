a = int(input().rstrip())

for i in range(a, 0, -1):
    print(" " * (2 * (a - i)), end='')
    print(" ".join('*' * (2 * i - 1)))