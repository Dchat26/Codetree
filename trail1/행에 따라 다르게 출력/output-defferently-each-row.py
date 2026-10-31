a = int(input().rstrip())

cnt = 0
for i in range(a):
    for _ in range(a):
        if i % 2 == 0:
            cnt += 1
            print(cnt, end=' ')
        else:
            cnt += 2
            print(cnt, end=' ')
    print()