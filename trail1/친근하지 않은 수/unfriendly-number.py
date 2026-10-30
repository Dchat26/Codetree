a = int(input().rstrip())

answer = 0
for i in range(1, a + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    else:
        answer += 1

print(answer)