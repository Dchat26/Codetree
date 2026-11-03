a = input().rstrip()
b = int(input().rstrip())

if len(a) < b:
    print(a[::-1])
else:
    for i in range(-1, -b - 1, -1):
        print(a[i], end='')