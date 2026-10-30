n = int(input().rstrip())

temp = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        temp += i
        temp += n // i

if temp - n == n:
    print("P")
else:
    print("N")