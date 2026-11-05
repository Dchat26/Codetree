def f(a):
    if a == 0:
        return
    
    f(a - 1)
    print('*' * a)


a = int(input().rstrip())

f(a)