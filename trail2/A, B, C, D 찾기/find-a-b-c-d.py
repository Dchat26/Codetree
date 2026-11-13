from itertools import combinations

arr = list(map(int, input().split()))
arr.sort()

p = arr[-1]
for i in combinations(arr[:-1], 4):
    if sum(i) == p:
        a, b, c, d = sorted(i)
        if c <= a + b:
            if sum(i) - a - b - c in arr:
                print(a, b, c, d)
                break