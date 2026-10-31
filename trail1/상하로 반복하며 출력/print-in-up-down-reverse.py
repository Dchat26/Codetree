a = int(input().rstrip())

for i in range(1, a + 1):
    for j in range(a):
        if j % 2 == 0:
            print(i, end='')
        else:
            print(a - i + 1, end='')
    print()