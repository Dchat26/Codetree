a = int(input().rstrip())
alist = [int(input().rstrip()) for _ in range(a)]

if a == 1:
    print(1)
else:
    p = 0
    if alist[0] > 0:
        p = 1
    else:
        p = 0

    answer = 0
    temp = 1
    for i in range(1, a):
        if p:
            if alist[i] > 0 and alist[i-1] > 0:
                temp += 1
            else:
                answer = max(answer, temp)
                temp = 1
                if alist[i] > 0:
                    p = 1
                else:
                    p = 0
        else:
            if alist[i] < 0 and alist[i-1] < 0:
                temp += 1
            else:
                answer = max(answer, temp)
                temp = 1
                if alist[i] > 0:
                    p = 1
                else:
                    p = 0
    
    answer = max(answer, temp)

    print(answer)
