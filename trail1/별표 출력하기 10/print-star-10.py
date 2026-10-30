a = int(input().rstrip())

for i in range(2 * a):
    if i % 2 == 0:
        print(" ".join('*' * (1 + ( i // 2))))
    else:
        print(" ".join('*' * (a - (i - 1) // 2)))