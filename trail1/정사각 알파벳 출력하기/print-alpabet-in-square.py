a = int(input().rstrip())

cnt = 64
for _ in range(a):
    for _ in range(a):
        cnt += 1
        print(chr(cnt), end='')
    print()