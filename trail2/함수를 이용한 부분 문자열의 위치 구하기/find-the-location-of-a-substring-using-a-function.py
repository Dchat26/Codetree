a = input().rstrip()
b = input().rstrip()


def p(temp):
    if a[temp:temp + len(b)] == b:
        return True
    return False


is_TF = False
for i in range(len(a) - len(b) + 1):
    if p(i):
        is_TF = True
        break

if is_TF:
    print(i)
else:
    print(-1)