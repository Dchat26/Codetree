a = input().split()

answer = 0
for i in a:
    temp = ""
    for j in i:
        if j.isdigit():
            temp += j
        else:
            answer += int(temp)
            temp = ""
            break
    
    if temp:
        answer += int(temp)

print(answer)