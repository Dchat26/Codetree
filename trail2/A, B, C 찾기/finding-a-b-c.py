from itertools import combinations

arr = list(map(int, input().split()))
arr.sort()

p = arr[-1]
for i in combinations(arr[:-1], 3):
    a, b, c = sorted(i)
    if a + b in arr and a + c in arr and b + c in arr:
        print(a, b, c)
        break