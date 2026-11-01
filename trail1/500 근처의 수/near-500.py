a = list(map(int, input().split()))

b = 0
c = 1001
for i in a:
    if i < 500 and i > b:
        b = i
    
    if i > 500 and i < c:
        c = i

print(b, c)