n, m, p = map(int, input().split())
mlist = [tuple(input().split()) for _ in range(m)]

if mlist[p - 1][1] == '0':
    print()
else:
    member = [chr(i + 65) for i in range(n)]
    s = set()
    x = mlist[p - 1][1]
    for i in range(m):
        a, b = mlist[i]

        if i >= p - 1 or b == x:
            s.add(a)

    answer = []
    for i in member:
        if not i in s:
            answer.append(i)
    
    print(*answer)