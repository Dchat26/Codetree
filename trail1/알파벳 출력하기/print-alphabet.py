a = int(input().rstrip())

cnt = 64
for i in range(a):
    for j in range(i + 1):
        cnt += 1

        if cnt > 90:
            cnt = 65
        
        print(chr(cnt), end='')
    print()