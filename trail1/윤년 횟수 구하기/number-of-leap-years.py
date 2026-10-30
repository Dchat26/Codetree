a = int(input().rstrip())

answer = 0
for i in range(1, a + 1):
    if i % 4 == 0 and not (i % 100 == 0 and i % 400 != 0):
        answer += 1
    
print(answer)