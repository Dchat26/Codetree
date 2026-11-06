a = int(input().rstrip())

if a == 0:
    print(0)
else:
    answer = ""
    while a > 0:
        answer += str(a % 2)
        a //= 2

    print(answer[::-1])