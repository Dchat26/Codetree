import sys

a = list(map(int, input().split()))

answer = sys.maxsize
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        for k in range(len(a) - 1):
            for l in range(k + 1, len(a)):
                for n in range(len(a) - 1):
                    for m in range(n + 1, len(a)):
                        if len({i, j, k, l, n, m}) == 6:
                            a1 = a[i] + a[j]
                            b1 = a[k] + a[l]
                            c1 = a[n] + a[m]

                            max_val = max(a1, b1, c1)
                            min_val = min(a1, b1, c1)

                            answer = min(answer, max_val - min_val)

print(answer)