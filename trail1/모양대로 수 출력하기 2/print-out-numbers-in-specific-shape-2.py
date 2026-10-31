a = int(input().rstrip())

cnt = 2
for _ in range(a):
    for _ in range(a):
        if cnt > 9:
            cnt = 2
        
        print(cnt, end=' ')
        cnt += 2
    print()