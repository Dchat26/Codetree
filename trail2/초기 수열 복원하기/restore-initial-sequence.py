n = int(input())

if n == 1:
    print(1)
else:
    nlist = list(map(int, input().split()))

    for i in range(1, nlist[0]):
        result = [i]

        for j in nlist:
            result.append(j - result[-1])

        if not any(i <= 0 for i in result) and len(set(result)) == n:
            print(*result)
            break