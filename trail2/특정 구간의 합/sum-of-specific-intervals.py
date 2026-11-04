n, m = map(int, input().split())
nlist = list(map(int, input().split()))


def p(a, b):
    temp = 0
    for i in range(a - 1, b):
        temp += nlist[i]
    
    return temp


for _ in range(m):
    a, b = map(int, input().split())

    print(p(a, b))