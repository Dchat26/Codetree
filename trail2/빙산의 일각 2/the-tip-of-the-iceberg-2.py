import re

a = int(input().rstrip())
alist = [int(input().rstrip()) for _ in range(a)]
s = max(alist)

answer = 0
for i in range(0, s):
    result = ""
    for j in alist:
        if j > i:
            result += '1'
        else:
            result += '0'
        
    result = re.sub(r'1+', '1', result)
    answer = max(answer, result.count('1'))

print(answer)