a = int(input().rstrip())

alist = list(map(int, input().split()))

answer = [0] * 10
for i in alist:
    answer[i] += 1

for i in range(1, 10):
    print(answer[i])