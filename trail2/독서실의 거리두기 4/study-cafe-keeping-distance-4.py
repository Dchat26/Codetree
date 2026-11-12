import sys

a = int(input().rstrip())
n = [idx for idx, i in enumerate(input().rstrip()) if i == '1']

answer = -sys.maxsize
for i in range(a - 1):
    for j in range(i + 1, a):
        temp = [k for k in n]
        if not i in temp and not j in temp:
            temp.append(i)
            temp.append(j)
            temp.sort()

            temp2 = []
            for l in range(len(temp) - 1):
                temp2.append(temp[l+1] - temp[l])
            
            answer = max(answer, min(temp2))

print(answer)