start, end = map(int, input().split())

answer = 0
for i in range(start, end + 1):
    result = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j == i // j:
                result += 1
            else:
                result += 2
    
    if result == 3:
        answer += 1

print(answer)