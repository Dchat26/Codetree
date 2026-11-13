n = int(input())
blocks = [int(input()) for _ in range(n)]

p = sum(blocks) // n
answer = 0
for i in blocks:
    if i > p:
        answer += i - p

print(answer)