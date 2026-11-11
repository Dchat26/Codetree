A, B, C = map(int, input().split())

answer = 0
for i in range(C // A + 1):
    for j in range(C // B + 1):
        s = A * i + B * j
        if s > C:
            break
        
        answer = max(answer, s)
    
print(answer)