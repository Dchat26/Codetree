a, b = input().split()
b = int(b)

for _ in range(b):
    c = input().rstrip()

    if c == '1':
        a = a[1:] + a[0]
    elif c == '2':
        a = a[-1] + a[:-1]
    else:
        a = a[::-1]
    
    print(a)