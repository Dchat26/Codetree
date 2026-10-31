a = int(input().rstrip())

for i in range(1, a + 1):
    for j in range(1, a + 1):
        if (i + j) % 4 == 0:
            print((i, j), end='\n')
        else:
            print((i, j), end=' ')