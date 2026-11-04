def p(row, col):
    for _ in range(row):
        for _ in range(col):
            print(1, end='')
        print()


a, b = map(int, input().split())

p(a, b)