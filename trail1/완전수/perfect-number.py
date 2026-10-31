start, end = map(int, input().split())

answer = 0
for i in range(start, end + 1):
    if i == 1:
        continue
    
    result = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            result += j
            result += i // j
    
    if result == i:
        answer += 1

print(answer)