m1, d1, m2, d2 = map(int, input().split())

s = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

md1 = sum(num_of_days[i] for i in range(m1)) + d1
md2 = sum(num_of_days[i] for i in range(m2)) + d2

print(s[(md2 - md1) % 7])