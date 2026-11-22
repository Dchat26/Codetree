n, t = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = l + r + d           # 시계 방향 순서로 이어 붙이기
k = t % (3 * n)
belt = belt[-k:] + belt[:-k] if k else belt

print(*belt[:n])
print(*belt[n:2*n])
print(*belt[2*n:])