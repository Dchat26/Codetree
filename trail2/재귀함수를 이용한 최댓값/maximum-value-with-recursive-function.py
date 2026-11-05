a = int(input().rstrip())
alist = list(map(int, input().split()))


def f(a):
    if a == 0:
        return 0
    
    s = f(a - 1)
    if alist[a] > alist[s]:
        return a
    return s


print(alist[f(a - 1)])