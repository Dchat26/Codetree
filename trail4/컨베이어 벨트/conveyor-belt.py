n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = b[::-1]

while t:
    at = a[-1]
    bt = b[0]

    for i in range(n - 1, 0, -1):
        a[i] = a[i-1]
    
    for i in range(n - 1):
        b[i] = b[i+1]

    a[0] = bt
    b[-1] = at

    t -= 1

print(*a)
print(*b[::-1])