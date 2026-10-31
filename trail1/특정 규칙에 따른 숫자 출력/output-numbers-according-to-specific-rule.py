a = int(input().rstrip())

cnt = 0
for i in range(a):
    print("  " * i, end='')
    for j in range(a - i):
        cnt += 1

        if cnt > 9:
            cnt = 1
            
        print(cnt, end=' ')
    print()