a = int(input().rstrip())

cnt = 64
for i in range(a):
    print('  ' * i, end='')
    for j in range(a - i):
        cnt += 1

        if cnt > 90:
            cnt = 65
        
        print(chr(cnt), end=' ')
    print()