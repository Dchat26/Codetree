answer = 0
cnt = 0
for _ in range(10):
    a = int(input().rstrip())

    if 0 <= a and a <= 200:
        answer += a
        cnt += 1

print(f"{answer} {answer / cnt:.1f}")