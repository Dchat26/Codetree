a = int(input().rstrip())

for i in range(1, a + 1):
    if i == 1:
        continue
    
    is_TF = True
    for j in range(2, i):
        if i % j == 0:
            is_TF = False
            break
    
    if is_TF:
        print(i, end=' ')