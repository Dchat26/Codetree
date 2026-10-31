a = int(input().rstrip())

cnt = 9
for _ in range(a):
    for _ in range(a):
        if cnt == 0:
            cnt = 9
        
        print(cnt, end='')
        cnt -= 1
    print()