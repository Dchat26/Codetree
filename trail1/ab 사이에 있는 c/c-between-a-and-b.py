a, b, c = map(int, input().split())

is_TF = False
for i in range(a, b + 1):
    if i % c == 0:
        is_TF = True
        break

if is_TF:
    print("YES")
else:
    print("NO")