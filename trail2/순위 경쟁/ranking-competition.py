a = int(input().rstrip())
alist = [tuple(input().split()) for _ in range(a)]

answer = 0
cur = "ABC"
abcdict = {'A': 0, 'B': 0, 'C': 0}
for a, b in alist:
    b = int(b)

    abcdict[a] += b
    p = max(i for i in abcdict.values())
    result = ""
    for j, k in abcdict.items():
        if k == p:
            result += j
    
    if result != cur:
        answer += 1
        cur = result

print(answer)