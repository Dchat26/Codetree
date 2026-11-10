import sys

abilities = list(map(int, input().split()))

s = sum(abilities)
answer = sys.maxsize
for i in range(len(abilities) - 2):
    for j in range(i + 1, len(abilities) - 1):
        for k in range(j + 1, len(abilities)):
            a = abilities[i] + abilities[j] + abilities[k]

            answer = min(answer, abs((s - a) - a))

print(answer)