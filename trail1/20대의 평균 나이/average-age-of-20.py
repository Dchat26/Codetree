answer = 0
cnt = 0
while True:
    a = int(input().rstrip())

    if a // 10 != 2:
        print(f"{answer / cnt:.2f}")
        break
    else:
        answer += a
        cnt += 1