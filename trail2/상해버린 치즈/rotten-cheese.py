n, m, d, s = map(int, input().split())
dlist = [tuple(map(int, input().split())) for _ in range(d)]
slist = [tuple(map(int, input().split())) for _ in range(s)]

p = [0] * (m + 1)
for a, b in slist:
    temp = set()
    for c, cheese, e in dlist:
        if a == c and b > e:
            temp.add(cheese)

    for i in temp:
        p[i] += 1

result = [idx for idx, i in enumerate(p) if i == s]
answer = 0
for i in result:
    temp = set()
    for person, cheese, _ in dlist:
        if i == cheese:
            temp.add(person)

    answer = max(answer, len(temp))

print(answer)