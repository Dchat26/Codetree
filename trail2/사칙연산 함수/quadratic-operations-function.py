def add(a, c):
    return a + c


def sub(a, c):
    return a - c


def multiple(a, c):
    return a * c


def division(a, c):
    return a // c


a, b, c = input().split()
a, c = int(a), int(c)

if b == '+':
    print(f"{a} + {c} = {add(a, c)}")
elif b == '-':
    print(f"{a} - {c} = {sub(a, c)}")
elif b == '*':
    print(f"{a} * {c} = {multiple(a, c)}")
elif b == '/':
    print(f"{a} / {c} = {division(a, c)}")
else:
    print("False")