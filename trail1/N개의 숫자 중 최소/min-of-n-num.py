n = int(input().rstrip())
nlist = list(map(int, input().split()))

min_val = nlist[0]
for i in nlist[1:]:
    if min_val > i:
        min_val = i

print(min_val, nlist.count(min_val))