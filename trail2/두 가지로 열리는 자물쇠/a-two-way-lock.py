N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

answer = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            i1 = min(abs(a1 - i), N - abs(a1 - i))
            j1 = min(abs(b1 - j), N - abs(b1 - j))
            k1 = min(abs(c1 - k), N - abs(c1 - k))

            i2 = min(abs(a2 - i), N - abs(a2 - i))
            j2 = min(abs(b2 - j), N - abs(b2 - j))
            k2 = min(abs(c2 - k), N - abs(c2 - k))

            if i1 <= 2 and j1 <= 2 and k1 <= 2:
                answer += 1
            elif i2 <= 2 and j2 <= 2 and k2 <= 2:
                answer += 1

print(answer)