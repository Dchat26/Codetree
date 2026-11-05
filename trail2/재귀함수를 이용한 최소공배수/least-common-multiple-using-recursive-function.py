a = int(input().rstrip())
alist = list(map(int, input().split()))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def f(a):
    if a == 0:
        return
    
    f(a - 1)
    alist[a] = alist[a] * alist[a-1] // gcd(alist[a], alist[a-1])

    return


f(a - 1)
print(alist[-1])