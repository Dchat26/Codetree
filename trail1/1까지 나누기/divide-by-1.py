a = int(input().rstrip())

answer = 1
while (1):
    a //= answer

    if a <= 1:
        break
    else:
        answer += 1

print(answer)