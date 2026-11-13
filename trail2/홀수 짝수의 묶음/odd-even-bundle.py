N = int(input())
a = list(map(int, input().split()))
odd = sum(x % 2 for x in a)
even = N - odd

ans = 0
for k in range(1, N + 1):
    h = k // 2         
    ev = k - h     
    if odd < h or (odd - h) % 2 != 0:
        continue
    rest_odd = odd - h

    if even + rest_odd // 2 >= ev:
        ans = max(ans, k)
        
print(ans)