n = int(input().rstrip())

answer = 0
for _ in range(n):
    a = int(input().rstrip())

    if a % 2 == 1 and a % 3 == 0:
        answer += a

print(answer)