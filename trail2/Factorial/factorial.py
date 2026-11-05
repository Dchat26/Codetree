def f(a):
    if a == 1:
        return 1
    
    return a * f(a - 1)


a = int(input().rstrip())

print(f(a))