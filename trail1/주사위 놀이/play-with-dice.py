a = list(map(int, input().split()))

answer = [0] * 7
for i in a:
    answer[i] += 1

for i in range(1, 7):
    print(f"{i} - {answer[i]}")