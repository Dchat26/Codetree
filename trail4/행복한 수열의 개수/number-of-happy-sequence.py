import re

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    t = True
    t2 = True
    for j in range(n - m + 1):
        temp = set([grid[i][j+k] for k in range(m)])
        temp2 = set([grid[j+k][i] for k in range(m)])
        
        if t and len(temp) == 1:
            answer += 1
            t = False
        
        if t2 and len(temp2) == 1:
            answer += 1
            t2 = False

print(answer)