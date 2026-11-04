def p(a):
    if len(set(list(a))) == 1:
        return False
    return True


a = input().rstrip()

if p(a):
    print("Yes")
else:
    print("No")