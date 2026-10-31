a = int(input().rstrip())

cnt = 1
for _ in range(a):
    for _ in range(a):
        if cnt == 10:
            cnt = 1
        
        print(cnt, end='')
        cnt += 1
    print()