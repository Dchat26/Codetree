a = list(map(int, input().split()))

max_val = a[0]
min_val = a[0]
for i in a[1:]:
    if i == 999 or i == -999:
        break
    
    if max_val < i:
        max_val = i
    
    if min_val > i:
        min_val = i

print(max_val, min_val)