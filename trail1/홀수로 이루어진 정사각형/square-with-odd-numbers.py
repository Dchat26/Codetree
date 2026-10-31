a = int(input().rstrip())

for i in range(11, 12 + (a - 1) * 2, 2):
    for j in range(0, (a - 1) * 2 + 1, 2):
        print(i + j, end=' ')
    print()