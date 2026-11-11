a = int(input().rstrip())
b = input().rstrip()

for i in range(1, a + 1):
    temp = set()
    for j in range(a - i + 1):
        s = b[j:j+i]
        temp.add(s)

    if len(temp) == a - i + 1:
        print(i)
        break