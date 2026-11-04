def Is_TF(alist, blist):
    if len(alist) < len(blist):
        return False
    
    for i in range(len(alist) - len(blist) + 1):
        TF = True
        for j in range(len(blist)):
            if blist[j] != alist[i+j]:
                TF = False
                break
        
        if TF:
            return True


a, b = map(int, input().split())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

print("Yes" if Is_TF(alist, blist) else "No")