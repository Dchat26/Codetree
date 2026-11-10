import sys

a = list(map(int, input().split()))
s = sum(a)

answer = -1
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        for k in range(len(a) - 1):
            for l in range(k + 1, len(a)):
                if len({i, j, k, l}) == 4:
                    c = a[i] + a[j]
                    d = a[k] + a[l]
                    e = s - c - d
                    if c != d and d != e and c != e:
                        max_val = max(c, d, e)
                        min_val = min(c, d, e)

                        diff = max_val - min_val

                        if answer == -1:
                            answer = diff
                        else:
                            answer = min(answer, diff)

print(answer)