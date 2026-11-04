def TF(n):
    if n % 2 == 0 and sum(map(int, str(n))) % 5 == 0:
        print("Yes")
    else:
        print("No")


a = int(input().rstrip())

TF(a)