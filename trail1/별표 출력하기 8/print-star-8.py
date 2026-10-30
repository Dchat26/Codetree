a = int(input().rstrip())

for i in range(1, a + 1):
    if i % 2 == 1:
        print('*')
    else:
        print(" ".join('*' * i))