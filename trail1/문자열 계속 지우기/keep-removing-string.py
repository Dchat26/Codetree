a = input().rstrip()
b = input().rstrip()

result = a
while True:
    if b not in a:
        break
    
    aidx = a.index(b)

    a = a[:aidx] + a[aidx+len(b):]

print(a)