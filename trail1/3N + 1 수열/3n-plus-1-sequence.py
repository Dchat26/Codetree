a = int(input().rstrip())

cnt = 0
while True:
    if a == 1:
        print(cnt)
        break
    else:
        cnt += 1

        if a % 2 == 0:
            a //= 2
        else:
            a = a * 3 + 1