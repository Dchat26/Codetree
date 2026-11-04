def Year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False


def Is_TF(op, m, d):
    if op:
        if m == 2:
            if d <= 29:
                return True
            return False
        elif m in (4, 6, 9, 11):
            if d <= 30:
                return True
            return False
        else:
            if d <= 31:
                return True
            return False
    else:
        if m == 2:
            if d <= 28:
                return True
            return False
        elif m in (4, 6, 9, 11):
            if d <= 30:
                return True
            return False
        else:
            if d <= 31:
                return True
            return False


def Season(m):
    if 3 <= m and m <= 5:
        return "Spring"
    elif 6 <= m and m <= 8:
        return "Summer"
    elif 9 <= m and m <= 11:
        return "Fall"
    else:
        return "Winter"


y, m, d = map(int, input().split())

if Year(y):
    if Is_TF(1, m, d):
        print(Season(m))
    else:
        print(-1)
else:
    if Is_TF(0, m, d):
        print(Season(m))
    else:
        print(-1)