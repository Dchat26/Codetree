def f(a):
    if a == 1:
        return 1
    
    if a == 2:
        return 1
    
    return f(a - 1) + f(a - 2)


a = int(input().rstrip())

print(f(a))