a = int(input().rstrip())
blist = list(map(int, input().split()))
clist = list(map(int, input().split()))

blist.sort()
clist.sort()

if len(blist) == len(clist):
    is_TF = False
    for a, b in zip(blist, clist):
        if a != b:
            is_TF = True
            break
    
    if is_TF:
        print("No")
    else:
        print("Yes")
else:
    print("No")