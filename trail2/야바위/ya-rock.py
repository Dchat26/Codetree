a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = 0
for i in range(3):
    cup = [0, 0, 0]
    cup[i] = 1
    score = 0
    for j, k, c in alist:
        temp = cup[j-1]
        cup[j-1] = cup[k-1]
        cup[k-1] = temp

        if cup[c-1] == 1:
            score += 1
    
    answer = max(answer, score)

print(answer)