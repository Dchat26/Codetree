import sys

a = int(input().rstrip())
alist = [int(input().rstrip()) for _ in range(a)]

min_val = sys.maxsize
for i in range(a):
    temp = 0
    p = (a - i) % a
    for j in range(a):
        temp += alist[j] * p

        if p == a - 1:
            p = 0
        else:
            p += 1
    
    min_val = min(min_val, temp)

print(min_val)