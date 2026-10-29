a = int(input().rstrip())

for i in range(1, a + 1):
    if i % 3 == 0 or any(j in str(i) for j in '369'):
        print(0, end=' ')
    else:
        print(i, end=' ')