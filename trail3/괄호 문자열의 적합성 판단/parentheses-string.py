a = input().rstrip()

s = []
ok = True
for i in a:
    if i == '(':
        s.append(i)
    elif i == ')':
        if s:
            s.pop()
        else:
            ok = False
            break

if s or not ok:
    print("No")
else:
    print("Yes")