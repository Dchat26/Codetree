k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            is_TF = True
            for k in arr:
                if k.index(i) > k.index(j):
                    is_TF = False
                    break
            
            if is_TF:
                answer += 1

print(answer)