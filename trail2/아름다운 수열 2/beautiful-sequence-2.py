N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if M > N:
    print(0)
else:
    temp = {}

    for i in B:
        temp[i] = temp.get(i, 0) + 1

    for i in range(M):
        temp[A[i]] = temp.get(A[i], 0) - 1

    count = sum(1 for v in temp.values() if v != 0)

    answer = 0

    if count == 0:
        answer += 1

    for i in range(M, N):
        out = A[i-M]
        new = A[i]

        before = temp.get(out, 0)
        temp[out] = before + 1

        if before == 0:
            count += 1
        elif before == -1:
            count -= 1

        before = temp.get(new, 0)
        temp[new] = before - 1

        if before == 0:
            count += 1
        elif before == 1:
            count -= 1

        if count == 0:
            answer += 1

    print(answer)