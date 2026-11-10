N, K = map(int, input().split())
Nlist = [tuple(map(int, input().split())) for _ in range(N)]

line = [0] * 101

for a, x in Nlist:
    line[x] += a

answer = 0
for i in range(101):
    temp = 0

    for j in range(max(0, i - K), min(100, i + K) + 1):
        temp += line[j]

    answer = max(answer, temp)

print(answer)