N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

p = [-1] * (N + 1)

p[P] = K
for _, b, c in sorted(handshakes, key=lambda x: x[0]):
    tb = p[b] > 0
    tc = p[c] > 0

    if tb:
        p[b] -= 1
    
    if tc:
        p[c] -= 1
    
    if tb and p[c] == -1:
        p[c] = K
    elif tc and p[b] == -1:
        p[b] = K 
    
result = ""
for i in p[1:]:
    if i >= 0:
        result += "1"
    else:
        result += "0"

print(result)