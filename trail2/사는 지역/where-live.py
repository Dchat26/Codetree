class p:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city


a = int(input().rstrip())

ps = []
for _ in range(a):
    a, b, c = input().split()

    ps.append(p(a, b, c))

ps.sort(key=lambda x: x.name, reverse=True)

print(f"name {ps[0].name}\naddr {ps[0].addr}\ncity {ps[0].city}")