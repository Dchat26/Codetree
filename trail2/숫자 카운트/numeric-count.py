n = int(input())
a, b, c = [], [], []

for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue

            is_TF = True
            for ai, bj, ck in zip(a, b, c):
                c1, c2 = 0, 0
                ai1, ai2, ai3 = map(int, str(ai))

                if ai1 == i:
                    c1 += 1
                if ai2 == j:
                    c1 += 1
                if ai3 == k:
                    c1 += 1

                if i != ai1 and i in (ai1, ai2, ai3):
                    c2 += 1
                if j != ai2 and j in (ai1, ai2, ai3):
                    c2 += 1
                if k != ai3 and k in (ai1, ai2, ai3):
                    c2 += 1

                if c1 != bj or c2 != ck:
                    is_TF = False
                    break

            if is_TF:
                answer += 1

print(answer)