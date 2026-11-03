a = input().rstrip()

b = ord(a) + 1
if b > 122:
    print(chr(b % 122 + 96))
else:
    print(chr(b))