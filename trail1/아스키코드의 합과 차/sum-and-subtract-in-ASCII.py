a, b = tuple(input().split())

print(ord(a) + ord(b), ord(max(a, b)) - ord(min(a, b)))