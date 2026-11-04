n, m = map(int, input().split())
nlist = list(map(int, input().split()))


def p():
    global m

    if m % 2 == 0:
        m //= 2
    else:
        m -= 1


answer = nlist[m-1]
while m > 1:
    p()

    answer += nlist[m-1]

print(answer)