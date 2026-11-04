def p(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if num > 9:
                num = 1
            
            print(num, end=' ')
            num += 1
        print()


a = int(input().rstrip())

p(a)