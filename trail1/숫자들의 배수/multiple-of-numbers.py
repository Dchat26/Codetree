a = int(input().rstrip())

p = 0
aval = a
while p < 2:
    print(aval, end=' ')

    if aval % 5 == 0:
        p += 1
    
    aval += a