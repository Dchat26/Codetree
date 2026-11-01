a = list(map(int, input().split()))

result = []
for i in a:
    if i == 0:
        break
    else:
        result.append(i)

print(result[-1] + result[-2] + result[-3])