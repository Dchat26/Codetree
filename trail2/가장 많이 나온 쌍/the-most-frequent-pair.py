a, b = map(int, input().split())
blist = [tuple(map(int, input().split())) for _ in range(b)]

answer = 0
for i in range(1, a):
    for j in range(i + 1, a + 1):
        temp = 0
        for c, d in blist:
            if (i == c and j == d) or (j == c and i == d):
                temp += 1
        
        answer = max(answer, temp)

print(answer)