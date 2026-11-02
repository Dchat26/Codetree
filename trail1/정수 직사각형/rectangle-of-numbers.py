a, b = map(int, input().split())

answer = [[0] * b for _ in range(a)]

for i in range(1, a * b + 1):
    answer[(i - 1) // b][(i - 1) % b] = i

for i in answer:
    print(*i)