def p(n):
    if n == n[::-1]:
        return True
    return False


a = input().rstrip()

if p(a):
    print("Yes")
else:
    print("No")