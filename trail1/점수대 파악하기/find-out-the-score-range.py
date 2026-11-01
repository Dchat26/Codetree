a = list(map(int, input().split()))

answer = [0] * 11
for i in a:
    if i == 0:
        break

    answer[i // 10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {answer[i]}")