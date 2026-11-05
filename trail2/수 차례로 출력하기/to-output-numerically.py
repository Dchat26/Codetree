def f(a):
    if a == 0:
        return

    f(a - 1)
    print(a, end=' ')


def rf(a):
    if a == 0:
        return

    print(a, end=' ')
    rf(a - 1)


a = int(input().rstrip())

f(a)
print()
rf(a)