N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = max(B)
line = [0] * (s + 1)

for i in B:
    line[i] += 1

answer = 0

for i in range(len(A) - len(B) + 1):
    is_TF = True
    temp = line.copy()

    for j in range(len(B)):
        if A[i+j] <= s and temp[A[i+j]] > 0:
            temp[A[i+j]] -= 1
        else:
            is_TF = False
            break

    if is_TF:
        answer += 1

print(answer)