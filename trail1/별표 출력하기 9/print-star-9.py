a = int(input().rstrip())

for i in range(1, a + 1):
    print(" " * (2 * (a - i)), end='')
    print(" ".join('*' * (2 * i - 1)))