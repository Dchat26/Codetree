a, b = map(int, input().split())

for i in range(a):
    for j in range(b):
        if j % 2 == 0:
            print(i + a * j, end=' ')
        else:
            print(a * j + a - i - 1, end=' ')
    print()