from itertools import combinations

nums = list(map(int, input().split()))
nums.sort()

for i in combinations(nums, 4):
    result = []
    for j in combinations(i, 2):
        result.append(sum(j))

    for j in combinations(i, 3):
        result.append(sum(j))

    result.append(sum(i))
    result.extend(i)

    result.sort()
    if nums == result:
        print(*i)
        break