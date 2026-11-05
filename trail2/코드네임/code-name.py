MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

users.sort(key=lambda x: x[1])

code, s = users[0]
print(code, s)