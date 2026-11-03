a = [input().rstrip() for _ in range(2)]

answer = 0
for i in a:
    temp = ""
    for j in i:
        if j.isdigit():
            temp += j
    
    answer += int(temp)

print(answer)