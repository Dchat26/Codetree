N, C, G, H = map(int, input().split())
Nlist = [tuple(map(int, input().split())) for _ in range(N)]

Nmax = max(i for _, i in Nlist)
Nmin = min(i for i, _ in Nlist)

answer = 0
for i in range(Nmin - 1, Nmax + 2):
    temp = 0
    for a, b in Nlist:
        if i < a:
            temp += C
        elif a <= i <= b:
            temp += G
        else:
            temp += H
    
    answer = max(answer, temp)

print(answer)