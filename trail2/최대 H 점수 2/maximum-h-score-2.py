N, L = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
for h in range(1, N + 1):
    ge = sum(1 for x in a if x >= h)        # 이미 h 이상인 원소 수
    one_less = sum(1 for x in a if x == h - 1)  # +1 하면 h가 되는 원소 수
    need = h - ge                            # 더 필요한 개수
    if need <= 0 or (need <= one_less and need <= L):
        answer = h

print(answer)