alist = list(map(int, input().split()))

answer = 0
v = 0
for idx, i in enumerate(alist):
    if i == 0:
        v = idx
        break
    else:
        answer += i
        v = idx + 1

print(f"{answer} {answer / v:.1f}")