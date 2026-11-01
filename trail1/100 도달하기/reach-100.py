a = int(input().rstrip())

p = 1
pp = a
print(p, pp, end=' ')
while pp < 100:
    p, pp = pp, p + pp

    print(pp, end=' ')