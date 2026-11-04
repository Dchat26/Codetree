def is_TF(n):
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    elif n % 4 == 0:
        return "true"
    else:
        return "false"


a = int(input().rstrip())

print(is_TF(a))