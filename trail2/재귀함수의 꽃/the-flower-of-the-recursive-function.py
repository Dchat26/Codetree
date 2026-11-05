def f(a):
    if a == 0:
        return
    
    print(a, end=' ')
    f(a - 1)
    print(a, end=' ')


a = int(input().rstrip())

f(a)