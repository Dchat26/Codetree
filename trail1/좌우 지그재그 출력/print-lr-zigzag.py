a = int(input().rstrip())

for i in range(a):
    for j in range(a):
        if i % 2 == 0:
            print(i * a + 1 + j, end=' ')
        else:
            print((i + 1) * a - j, end=' ')
    print()
