n = int(input().rstrip())
nlist = list(map(int, input().split()))

if len(set(nlist)) == 1:
    print(-1)
else:
    p = sorted(set(nlist))[1]

    if nlist.count(p) >= 2:
        print(-1)
    else:
        for idx, i in enumerate(nlist):
            if i == p:
                print(idx + 1)
                break