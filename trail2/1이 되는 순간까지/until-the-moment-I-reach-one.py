def f(a):
    if a == 1:
        return 0
    
    if a % 2 == 0:
        return 1 + f(a // 2)
    else:
        return 1 + f(a // 3)


a = int(input().rstrip())

answer = f(a)

print(answer)