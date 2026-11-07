a = int(input().rstrip())
alist = [int(input().rstrip()) for _ in range(a)]

if a == 1:
    print(1)
else:
    answer = 0
    temp = 1
    for i in range(1, a):
        if alist[i] == alist[i-1]:
            temp += 1
        else:
            answer = max(answer, temp)
            temp = 1

    answer = max(answer, temp)
    
    print(answer)