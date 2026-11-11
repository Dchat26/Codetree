a, b = map(int, input().split())

answer = 0
for i in range(a, b + 1):
    temp = 0
    for j in str(i):
        temp += int(j)
    
    answer = max(answer, temp)

print(answer)