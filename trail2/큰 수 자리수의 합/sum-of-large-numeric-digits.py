def f(n):
    if n < 10:
        return n
    
    return n % 10 + f(n // 10)


a, b, c  = map(int, input().split())

print(f(a * b * c))