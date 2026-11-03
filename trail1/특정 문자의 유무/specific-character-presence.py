a = input().rstrip()

if "ee" in a and "ab" in a:
    print("Yes Yes")
elif "ee" in a:
    print("Yes No")
elif "ab" in a:
    print("No Yes")
else:
    print("No No")