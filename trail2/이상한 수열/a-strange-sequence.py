def f(a):
    if a == 1 or a == 2:
        return a
    
    return f(a // 3) + f(a - 1)


a = int(input().rstrip())

print(f(a))