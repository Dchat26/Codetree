m1, d1, m2, d2 = map(int, input().split())
A = input()

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

md1 = sum(days[i] for i in range(m1)) + d1
md2 = sum(days[i] for i in range(m2)) + d2

if (md2 - md1) % 7 < d.index(A):
    print((md2 - md1) // 7)
else:
    print((md2 - md1) // 7 + 1)