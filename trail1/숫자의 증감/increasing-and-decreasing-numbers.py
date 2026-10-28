a, b = input().split()
b = int(b)

if a == 'A':
    for i in range(1, b + 1):
        print(i, end=' ')
else:
    for i in range(b, 0, -1):
        print(i, end=' ')