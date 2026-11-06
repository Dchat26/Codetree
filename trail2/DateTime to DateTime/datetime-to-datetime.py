d, h, m = map(int, input().split())

dhm1 = d * 1440 + h * 60 + m
dhm2 = 11 * 1440 + 11 * 60 + 11

if dhm1 - dhm2 < 0:
    print(-1)
else:
    print(dhm1 - dhm2)