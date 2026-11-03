a = input().rstrip()
astr = "".join(input().split())

for i in range(0, len(astr), 5):
    print(astr[i:i+5])