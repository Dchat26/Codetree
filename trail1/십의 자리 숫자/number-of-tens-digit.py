a = list(map(int, input().split()))

answer = [0] * 10
for i in a:
    if i == 0:
        break
        
    answer[i // 10] += 1

for i in range(1, 10):
    print(f"{i} - {answer[i]}")