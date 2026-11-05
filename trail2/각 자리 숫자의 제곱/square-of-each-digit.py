def f(a):
    if a < 10:
        return a ** 2
    
    return (a % 10) ** 2 + f(a // 10)


a = int(input().rstrip())

answer = f(a)

print(answer)