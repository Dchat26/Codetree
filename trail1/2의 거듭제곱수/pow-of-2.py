a = int(input().rstrip())

cnt = 0
while True:
    cnt += 1
    a //= 2

    if a == 1:
        print(cnt)
        break