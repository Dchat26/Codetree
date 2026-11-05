def f(a):
    if a == 2:
        return 2
    
    return a + f(a - 2)


def rf(a):
    if a == 1:
        return 1
    
    return a + rf(a - 2)


a = int(input().rstrip())

if a % 2 == 0:
    print(f(a))
else:
    print(rf(a))