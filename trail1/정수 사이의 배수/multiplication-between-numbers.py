a, b = map(int, input().split())

answer = 0
cnt = 0
for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        answer += i
        cnt += 1

print(f"{answer} {answer / cnt:.1f}")