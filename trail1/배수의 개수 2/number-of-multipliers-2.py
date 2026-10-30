answer = 0
for _ in range(10):
    a = int(input().rstrip())

    if a % 2 == 1:
        answer += 1

print(answer)