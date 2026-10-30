answer = 0
for _ in range(5):
    a = int(input().rstrip())

    if a % 2 == 0:
        answer += 1

print(answer)