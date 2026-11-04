def Is_TF(a, b):
    if a > 12 or b > 31:
        return False
    
    if a == 2:
        if b <= 28:
            return True
        return False
    elif a in (4, 6, 9, 11):
        if b <= 30:
            return True
        return False
    else:
        if b <= 31:
            return True
        return False


a, b = map(int, input().split())

if Is_TF(a, b):
    print("Yes")
else:
    print("No")