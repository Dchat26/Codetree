class Weather:
    def __init__(self, y, d, w):
        self.y = y
        self.d = d
        self.w = w


a = int(input().rstrip())

weathers = []
for _ in range(a):
    a, b, c = input().split()

    weathers.append(Weather(a, b, c))

weathers.sort(key=lambda x: x.y)

for i in weathers:
    if i.w == "Rain":
        print(i.y, i.d, i.w)
        break