N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

result = set()
for i in range(N - 1):
    for j in range(i + 1, N):
        if num[i] == num[j] and j - i <= K:
            result.add(i)
            result.add(j)

rdict = {}
for i in result:
    rdict[num[i]] = rdict.get(num[i], 0) + 1

if rdict:
    print(max(rdict, key=lambda x: (rdict[x], x)))
else:
    print(0)