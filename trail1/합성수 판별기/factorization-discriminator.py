a = int(input().rstrip())

is_TF = False
for i in range(2, a):
    if a % i == 0:
        is_TF = True
        break

if is_TF:
    print('C')
else:
    print('N')