a = input().rstrip()

ee = 0
eb = 0
for i in range(len(a) - 1):
    s = a[i] + a[i+1]
    if s == "ee":
        ee += 1

    if s == "eb":
        eb += 1

print(ee, eb)