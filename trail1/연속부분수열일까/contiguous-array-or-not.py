a, b = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

is_TF = False
if blist[0] not in alist:
    print("No")
else:
    idx = alist.index(blist[0])
    aval = alist[idx:]
    if len(aval) < b:
        print("No")
    else:
        for i in range(len(aval) - b + 1):
            is_TF2 = True
            for j in range(b):
                if blist[j] != aval[i+j]:
                    is_TF2 = False
                    break
            
            if is_TF2:
                is_TF = True
                break
        
        if is_TF:
            print("Yes")
        else:
            print("No")