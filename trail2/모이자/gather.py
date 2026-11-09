import sys

a = int(input().rstrip())
alist = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(a):       
    temp = 0             
    p = i
    x = 0
    for j in alist:
        temp += j * p

        if p == 0:
            x = 1

        if x:
            p += 1
        else:
            p -= 1
    
    min_val = min(min_val, temp)

print(min_val)