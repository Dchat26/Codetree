a = int(input().rstrip())
n = input().rstrip()

result = [idx for idx, i in enumerate(n) if i == '1']
answer = 0
for i in range(a):
    temp = [j for j in result]
    if not i in temp:
        temp.append(i)
        temp.sort()

        temp2 = []
        for k in range(len(temp) - 1):
            temp2.append(temp[k+1] - temp[k])

        answer = max(answer, min(temp2))

print(answer)