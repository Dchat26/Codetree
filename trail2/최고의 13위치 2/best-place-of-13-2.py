n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and not (j + 2 < l or l + 2 < j):
                    continue
                
                temp = 0
                for m in range(3):
                    temp += arr[i][j+m] + arr[k][l+m]
                
                answer = max(answer, temp)

print(answer)