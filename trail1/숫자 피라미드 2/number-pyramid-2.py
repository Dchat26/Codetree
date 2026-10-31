a = int(input().rstrip())

cnt = 0
for i in range(a):
    for j in range(i + 1):
        cnt += 1
        print(cnt, end=' ')
    print()