a = int(input().rstrip())

alist = list(map(float, input().split()))

score = sum(alist) / a

if score >= 4.0:
    print(f"{score:.1f}\nPerfect")
elif score >= 3.0:
    print(f"{score:.1f}\nGood")
else:
    print(f"{score:.1f}\nPoor")