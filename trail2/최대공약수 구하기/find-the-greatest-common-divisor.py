def g(c, d):
    while d:
        c, d = d, c % d
    
    print(c)


a, b = map(int, input().split())

g(a, b)