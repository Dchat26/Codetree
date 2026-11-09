import sys

a = int(input().rstrip())
alist = [int(input().rstrip()) for _ in range(a)]

answer = -1
for i in range(a - 2):
    for j in range(i + 1, a - 1):
        for k in range(j + 1, a):
            l, m, n = alist[i], alist[j], alist[k]
            is_TF = True
            while True:
                if l == 0 and m == 0 and n == 0:
                    break 

                if l % 10 + m % 10 + n % 10 >= 10:
                    is_TF = False
                    break
                
                l //= 10
                m //= 10
                n //= 10
            
            if is_TF:
                answer = max(answer, alist[i] + alist[j] + alist[k])
    
print(answer)