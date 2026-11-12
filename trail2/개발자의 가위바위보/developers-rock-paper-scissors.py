N = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(N)]
rsp = [(3, 1, 2), (2, 3, 1)]

a1 = 0
a2 = 0
for a, b in nlist:
    if rsp[0][a-1] == b:
        a1 += 1
    
    if rsp[1][a-1] == b:
        a2 += 1

print(max(a1, a2))