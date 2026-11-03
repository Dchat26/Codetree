acount = 0
alist = []
while True:
    a = input().rstrip()

    if a == '0':
        break
    
    acount += 1
    alist.append(a)

print(acount)
for idx, i in enumerate(alist):
    if idx % 2 == 0:
        print(i)