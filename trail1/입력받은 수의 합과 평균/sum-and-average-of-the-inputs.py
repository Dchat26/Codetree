n = int(input().rstrip())

answer = 0
for _ in range(n):
    a = int(input().rstrip())
    answer += a

print(f"{answer} {answer / n:.1f}")