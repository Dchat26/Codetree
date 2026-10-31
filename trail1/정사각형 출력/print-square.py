a = int(input().rstrip())

for i in range(1, a * a + 1):
    if i % a == 0:
        print(i)
    else:
        print(i, end=' ')