a = input().rstrip()

for i in range(len(a) - 1, 0, -1):
    if i % 2 == 1:
        print(a[i], end='')