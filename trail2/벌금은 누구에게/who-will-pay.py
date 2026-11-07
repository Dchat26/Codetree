N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

nk = [0] * (N + 1)
answer = -1
for i in student:
    nk[i] += 1

    if nk[i] >= K:
        answer = i
        break

print(answer)